from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import fitsio
import desimodel.io
import desitarget.mtl
import desisim.quickcat
from astropy.io import fits
from astropy.table import Table, Column, vstack
import json
import shutil
import healpy
from desitarget.targetmask import desi_mask, obsconditions
from collections import Counter
import subprocess

    
def consolidate_favail(fba_files):
    # getting all the targetids of the assigned fibers
    print('reading individual fiberassign files')
    favail = list()
    for i_tile, tile_file in enumerate(fba_files):
        if i_tile%50 ==0:
            print(i_tile)
        id_favail, header = fits.getdata(tile_file, 'FAVAIL', header=True)
        favail.extend(id_favail['TARGETID'])
    return list(set(favail))
    


    
def old():
    for i_pass in range(len(footprint_names)-1):
    
        footprint_name = footprint_names[i_pass]
        old_pass_name = pass_names[i_pass-1]
        pass_name = pass_names[i_pass]
        new_pass_name = pass_names[i_pass+1]
    
        os.makedirs('{}/fiberassign_{}'.format(strategy, pass_name), exist_ok=True)
        os.makedirs('{}/targets'.format(strategy), exist_ok=True)
        os.makedirs('{}/zcat'.format(strategy), exist_ok=True)

    
        assign_footprint_filename = 'footprint/subset_{}.fits'.format(footprint_name)
        zcat_footprint_filename = 'footprint/subset_{}.fits'.format(pass_name)
        fiberassign_dir = '{}/fiberassign_{}/'.format(strategy, pass_name)
        mtl_filename = '{}/targets/{}_subset_dr8_mtl_dark_gray_NGC.fits'.format(strategy, pass_name)
        new_mtl_filename = '{}/targets/{}_subset_dr8_mtl_dark_gray_NGC.fits'.format(strategy, new_pass_name)
        old_zcat_filename = '{}/zcat/{}_zcat.fits'.format(strategy, old_pass_name)
        zcat_filename = '{}/zcat/{}_zcat.fits'.format(strategy, pass_name)
    
        if i_pass == 0:
            shutil.copyfile(initial_mtl_file, mtl_filename)
        
    
        # Run fiberassign
 
        if legacy==True:
            cmd = '{} --mtl {} --sky {} --std {}'.format(fiberassign_script, mtl_filename, initial_sky_file, initial_std_file)
            cmd += ' --footprint {} --outdir {} --overwrite '.format(assign_footprint_filename, fiberassign_dir)
            cmd += ' --fibstatusfile fiberstatus.ecsv --starmask 60129542144'
        if legacy==False:
            cmd = 'fiberassign --mtl {} --sky targets/subset_dr8_sky.fits '.format(mtl_filename)
            cmd +=' --footprint {} --outdir {} --overwrite'.format(assign_footprint_filename, fiberassign_dir)
            
        print(cmd)
        os.system(cmd)
    
        # Gather fiberassign files
        fba_files = np.sort(glob.glob(os.path.join(fiberassign_dir,"fiberassign*.fits")))

        # remove tilefiles that are not in the list of tiles to build zcat
        footprint = Table.read(zcat_footprint_filename)
        to_keep = []
        for i_file, fba_file in enumerate(fba_files):
            fibassign, header = fits.getdata(fba_file, header=True)
            tileid = int(header['TILEID'])
            if tileid in footprint['TILEID']:
                print(tileid, 'in list', zcat_footprint_filename)
                print('keeping {}'.format(fba_file))
                to_keep.append(i_file)
            else:
                print('renaming {}'.format(fba_file))
                fiberassign_file = fba_file.replace('fiberassign-', 'fba_')
                renamed_file = fiberassign_file.replace('.fits', '_unused.fits')
                print('renaming', fba_file, renamed_file)
                os.rename(fba_file, renamed_file)
            
        fba_files = fba_files[to_keep]
        print('Files to keep', len(fba_files))
    
        # Read targets and truth
        targets = Table.read(mtl_filename)
        truth = Table.read(initial_truth_file)
    
        # Compute zcat
        if i_pass==0:
            zcat = desisim.quickcat.quickcat(fba_files, targets, truth, perfect=True)
        else:
            old_zcat = Table.read(old_zcat_filename)
            zcat = desisim.quickcat.quickcat(fba_files, targets, truth, zcat=old_zcat, perfect=True)        
    
        zcat.write(zcat_filename, overwrite=True)
        mtl = desitarget.mtl.make_mtl(targets, obsconditions[i_pass], zcat=zcat)
        mtl.write(new_mtl_filename, overwrite=True)

def run_strategy(initial_mtl_file, truth_file, sky_file, output_path="./", batch_path="./", program='dark'):
    os.makedirs(output_path, exist_ok=True)
    targets_path='{}/targets'.format(output_path)
    zcat_path = '{}/zcat'.format(output_path)
    os.makedirs(targets_path, exist_ok=True)
    os.makedirs(zcat_path, exist_ok=True)
    os.makedirs('{}/fiberassign'.format(output_path), exist_ok=True)

    batch_files = glob.glob(batch_path+"/batch_*_"+program+".fits")
    batch_files.sort()
    
    # Read targets and truth
    targets = Table.read(mtl_filename)
    truth = Table.read(truth_file)
    
    #obsconditions
    obsconditions = None
    if program=='dark':
        obsconditions = 'DARK|GRAY'
    if program=='bright':
        obsconditions = 'BRIGHT'
    
    n_batch = len(batch_files)
    for i_batch in range(2):
        print()
        print("Batch {}".format(i_batch))
        fiberassign_path = '{}/fiberassign/{:04d}'.format(output_path, i_batch)
        os.makedirs(fiberassign_path, exist_ok=True)

        footprint = batch_files[i_batch]
        mtl_filename = os.path.join(targets_path, '{:04d}_mtl.fits'.format(i_batch))
        new_mtl_filename = os.path.join(targets_path, '{:04d}_mtl.fits'.format(i_batch+1))

        zcat_filename = os.path.join(targets_path, '{:04d}_zcat.fits'.format(i_batch))
        old_zcat_filename = os.path.join(targets_path, '{:04d}_zcat.fits'.format(i_batch-1))
        
        
        if i_batch == 0:
            shutil.copyfile(initial_mtl_file, mtl_filename)
        print(footprint)
        
        fba_run = 'fba_run --targets {} --sky {} --footprint {}  --dir {} --rundate 2020-01-01T00:00:00 --overwrite'.format(
            mtl_filename, sky_file, footprint, fiberassign_path)
        print(fba_run)
        os.system(fba_run)
    
        # Gather fiberassign files
        fba_files = np.sort(glob.glob(os.path.join(fiberassign_path,"fba-*.fits")))
        
        # Compute zcat
        if i_pass==0:
            zcat = desisim.quickcat.quickcat(fba_files, targets, truth, fassignhdu='FASSIGN', perfect=True)
        else:
            old_zcat = Table.read(old_zcat_filename)
            zcat = desisim.quickcat.quickcat(fba_files, targets, truth, fassignhdu='FASSIGN', zcat=old_zcat, perfect=True)        
    
        zcat.write(zcat_filename, overwrite=True)
        mtl = desitarget.mtl.make_mtl(targets, obsconditions, zcat=zcat)
        mtl.write(new_mtl_filename, overwrite=True)
        

run_strategy("targets/patch_DR8_mtl_dark.fits", "targets/patch_DR8_truth_dark.fits", "targets/patch_DR8_sky.fits", 
             output_path="monthly_dark_patch_month", batch_path="footprint_patch_month", program="dark")