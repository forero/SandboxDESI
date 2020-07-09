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
    truth = Table.read(truth_file)
    
    #obsconditions
    obsconditions = None
    if program=='dark':
        obsconditions = 'DARK|GRAY'
    if program=='bright':
        obsconditions = 'BRIGHT'
    
    n_batch = len(batch_files)
    for i_batch in range(n_batch):
        print()
        print("Batch {}".format(i_batch))
        fiberassign_path = '{}/fiberassign/{:04d}'.format(output_path, i_batch)
        os.makedirs(fiberassign_path, exist_ok=True)

        footprint = batch_files[i_batch]
        mtl_filename = os.path.join(targets_path, '{:04d}_mtl.fits'.format(i_batch))
        new_mtl_filename = os.path.join(targets_path, '{:04d}_mtl.fits'.format(i_batch+1))

        zcat_filename = os.path.join(zcat_path, '{:04d}_zcat.fits'.format(i_batch))
        old_zcat_filename = os.path.join(zcat_path, '{:04d}_zcat.fits'.format(i_batch-1))
        
        
        if i_batch == 0:
            shutil.copyfile(initial_mtl_file, mtl_filename)
        print(footprint)
        
        fba_run = 'fba_run --targets {} --sky {} --footprint {}  --dir {} --rundate 2020-01-01T00:00:00 --overwrite'.format(
            mtl_filename, sky_file, footprint, fiberassign_path)
        print(fba_run)
        os.system(fba_run)
    
        # Gather fiberassign files
        fba_files = np.sort(glob.glob(os.path.join(fiberassign_path,"fba-*.fits")))
        
        # read the current mtl file
        targets = Table.read(mtl_filename)

        # Compute zcat
        if i_batch==0:
            zcat = desisim.quickcat.quickcat(fba_files, targets, truth, fassignhdu='FASSIGN', perfect=True)
        else:
            old_zcat = Table.read(old_zcat_filename)
            zcat = desisim.quickcat.quickcat(fba_files, targets, truth, fassignhdu='FASSIGN', zcat=old_zcat, perfect=True)        
    
        zcat.write(zcat_filename, overwrite=True)
        mtl = desitarget.mtl.make_mtl(targets, obsconditions, zcat=zcat)
        mtl.write(new_mtl_filename, overwrite=True)
        
        del mtl
        del targets
        del zcat
        

run_strategy("targets/patch_DR8_mtl_dark.fits", "targets/patch_DR8_truth_dark.fits", "targets/patch_DR8_sky.fits",
             output_path="dark_patch_semester", batch_path="footprint_patch_semester", program="dark")

run_strategy("targets/patch_DR8_mtl_dark.fits", "targets/patch_DR8_truth_dark.fits", "targets/patch_DR8_sky.fits", 
             output_path="dark_patch_month", batch_path="footprint_patch_month", program="dark")

run_strategy("targets/global_DR8_mtl_dark.fits", "targets/global_DR8_truth_dark.fits", "targets/global_DR8_sky.fits",
             output_path="dark_global_semester", batch_path="footprint_semester", program="dark")

run_strategy("targets/global_DR8_mtl_dark.fits", "targets/global_DR8_truth_dark.fits", "targets/global_DR8_sky.fits", 
             output_path="dark_global_month", batch_path="footprint_month", program="dark")