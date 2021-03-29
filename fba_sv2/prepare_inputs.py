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
from desitarget.sv2 import sv2_targetmask


def cut_tiles(tile_file, tile_path="./", cut_name="one_pct", limits={}):
    cut_tilefile = os.path.join(tile_path, cut_name + "_" + tile_file)

    # Create output directory
    if os.path.exists(cut_tilefile):
        print("Files {} already exist".format(cut_tilefile))
        return cut_tilefile
        
    os.makedirs(os.path.join(tile_path), exist_ok=True)
    
    tiles = Table.read(os.path.join(tile_path,tile_file))
        
    min_ra = limits['min_ra'] 
    max_ra = limits['max_ra'] 
    min_dec = limits['min_dec'] 
    max_dec = limits['max_dec'] 
    
    ii = (tiles['RA']>min_ra) & (tiles['RA']<max_ra) & (tiles['DEC']<max_dec) & (tiles['DEC']>min_dec) 
    tiles[ii].write(cut_tilefile, overwrite='True')
    print("Wrote tiles to {}".format(cut_tilefile))

    return cut_tilefile

    
def write_sky_file(output_path="./", limits={}):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    sky_file = os.path.join(output_path, "sky_onepct.fits")

    if os.path.exists(sky_file):
        print("Files {} already exist".format(sky_file))
        return sky_file
    
          
    min_ra = limits['min_ra'] 
    max_ra = limits['max_ra'] 
    min_dec = limits['min_dec'] 
    max_dec = limits['max_dec'] 
    
    
    # List all the fits files to read
    path_to_targets = '/global/cfs/projectdirs/desi/target/catalogs/dr9/0.53.0/skies/'
    target_files = glob.glob(os.path.join(path_to_targets, "skies-*.fits"))
    print('sky files to read:', len(target_files))
    target_files.sort()
    
    # Read the first file, only the columns that are useful for MTL
    data = fitsio.FITS(target_files[0], 'r')
    target_data = data[1].read()
    data.close()
    
    
    # Read all the other files
    for i, i_name in enumerate(target_files[1:]): 
        data = fitsio.FITS(i_name, 'r')
        tmp_data = data[1].read()
        ii_one_pct = (tmp_data['RA']>min_ra) & (tmp_data['RA']<max_ra) & (tmp_data['DEC']>min_dec) & (tmp_data['DEC']<max_dec) 
        if np.count_nonzero(ii_one_pct):
            target_data = np.hstack((target_data, tmp_data))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data), np.count_nonzero(ii_one_pct))

    target_data = Table(target_data)
    ii_one_pct = (target_data['RA']>min_ra) & (target_data['RA']<max_ra) & (target_data['DEC']>min_dec) & (target_data['DEC']<max_dec) 
    

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    print("Writing onepct sky")
    target_data[ii_one_pct].write(sky_file, overwrite=True)
    print("Wrote output to {}".format(sky_file))
   
    return sky_file


def write_onepct_mtl(output_path="./", program='bright', survey='main', limits={}):
              
    min_ra = limits['min_ra'] 
    max_ra = limits['max_ra'] 
    min_dec = limits['min_dec'] 
    max_dec = limits['max_dec'] 
    
    full_mtl_file = os.path.join(output_path, "mtl_{}_{}_onepct.fits".format(program, survey))
    
    if os.path.exists(full_mtl_file):
        print("Files {} already exist".format(full_mtl_file))
        return full_mtl_file

    # List all the fits files to read
    path_to_targets = '/global/cfs/cdirs/desi/target/catalogs/dr9/0.53.0/targets/' + survey +'/resolve/'+program+'/'
    target_files = glob.glob(os.path.join(path_to_targets, "*targets*fits"))
    print('target files to read:', len(target_files))
    target_files.sort()
    
    
    # Read the first file, only the columns that are useful for MTL
    data = fitsio.FITS(target_files[0], 'r')
    target_data = data[1].read()
    data.close()
    
    # Read all the other files
    for i, i_name in enumerate(target_files[1:]): 
        data = fitsio.FITS(i_name, 'r')
        tmp_data = data[1].read()
        ii_one_pct = (tmp_data['RA']>min_ra) & (tmp_data['RA']<max_ra) & (tmp_data['DEC']>min_dec) & (tmp_data['DEC']<max_dec) 
        if np.count_nonzero(ii_one_pct):
            target_data = np.hstack((target_data, tmp_data[ii_one_pct]))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data), np.count_nonzero(ii_one_pct))
    full_mtl = desitarget.mtl.make_mtl(target_data, 'DARK|GRAY|BRIGHT')

    ii_one_pct = (full_mtl['RA']>min_ra) & (full_mtl['RA']<max_ra) & (full_mtl['DEC']>min_dec) & (full_mtl['DEC']<max_dec) 

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    print("Writing {} full".format(program))
    full_mtl[ii_one_pct].write(full_mtl_file, overwrite=True)
    print("Wrote output to {}".format(full_mtl_file))
    
    return full_mtl_file

def update_onepct_mtl(filename, mask_name, qso_frac=0.82):
    output_filename = filename.replace('mtl', 'mtl_updated_qso_{:.2f}'.format(qso_frac))
    if os.path.exists(output_filename):
        print("Files {} already exist".format(output_filename))
        return output_filename
    
    data = Table.read(filename)
    print('finished reading', filename)
    isqso = (data[mask_name]&desi_mask['QSO'])!=0
    r = np.random.random(len(data))
    rr = r<qso_frac
    data['NUMOBS_INIT'][rr & isqso] = 1
    data['NUMOBS_MORE'][rr & isqso] = 1
    data.write(output_filename, overwrite=True)
    print('finished writing', output_filename)
    return output_filename


def update_bgs(filename):
    output_filename = filename.replace('mtl', 'mtl_updated_bgs')
    if os.path.exists(output_filename):
        print("Files {} already exist".format(output_filename))
        return output_filename    

    data = Table.read(filename)
    print(len(data))
    flux_r = data["FLUX_R"]/data["MW_TRANSMISSION_R"]
    flux_g = data["FLUX_G"]/data["MW_TRANSMISSION_G"]
    flux_z = data["FLUX_Z"]/data["MW_TRANSMISSION_Z"]
    flux_W1 = data["FLUX_W1"]/data["MW_TRANSMISSION_W1"]
    flux_W2 = data["FLUX_W2"]/data["MW_TRANSMISSION_W2"]
    fiber_r = data["FIBERFLUX_R"]/data["MW_TRANSMISSION_R"]

    gmag = 22.5 - 2.5 * np.log10(flux_g.clip(1e-7))
    rmag = 22.5 - 2.5 * np.log10(flux_r.clip(1e-7))
    zmag = 22.5 - 2.5 * np.log10(flux_z.clip(1e-7))
    w1mag = 22.5 - 2.5 * np.log10(flux_W1.clip(1e-7))
    w2mag = 22.5 - 2.5 * np.log10(flux_W2.clip(1e-7))
    rfibermag = 22.5 - 2.5 * np.log10(fiber_r.clip(1e-7))
    
    rr = np.random.random(len(data))
    
    is_bgs_main  = rmag < 19.5
    
    color = (zmag - w1mag) - 3.0/2.5 * (gmag - rmag) + 1.2
    rfiber_color_cut = (rfibermag < 20.75) | ((rfibermag < 21.5) & (color>0))
    
    is_bgs_faint = (rmag>19.5) & (rmag<20.3) & (rfiber_color_cut) & (rr < 0.66)

    is_bgs_hip = (rmag>19.5) & (rmag<20.3) & (rfiber_color_cut) & (~(rr < 0.66))
    
    is_bgs = is_bgs_main | is_bgs_faint | is_bgs_hip
    
    print(np.count_nonzero(is_bgs_main), np.count_nonzero(is_bgs_faint), np.count_nonzero(is_bgs_hip))
    was_bgs = (data['SV2_DESI_TARGET']&sv2_targetmask.desi_mask['BGS_ANY'])!=0

    
    data['PRIORITY_INIT'][was_bgs & is_bgs_faint] = 2000
    data['PRIORITY'][was_bgs & is_bgs_faint] = 2000
    data['PRIORITY_INIT'][was_bgs & is_bgs_hip] = 2100
    data['PRIORITY'][was_bgs & is_bgs_hip] = 2100
    data['PRIORITY_INIT'][was_bgs & is_bgs_main] = 2100
    data['PRIORITY'][was_bgs & is_bgs_main] = 2100
    data['NUMOBS_MORE'][was_bgs & is_bgs] = 1
    data['NUMOBS_INIT'][was_bgs & is_bgs] = 1

    ii = (data['SV2_DESI_TARGET']&sv2_targetmask.desi_mask['BGS_ANY'])!=0
    print(np.count_nonzero(was_bgs), np.count_nonzero(is_bgs))
    
    data['SV2_DESI_TARGET'][is_bgs] |= sv2_targetmask.desi_mask['BGS_ANY']
    data['SV2_BGS_TARGET'][~is_bgs] = 0
    data['SV2_BGS_TARGET'][is_bgs_faint] = sv2_targetmask.bgs_mask['BGS_FAINT']
    data['SV2_BGS_TARGET'][is_bgs_hip] = sv2_targetmask.bgs_mask['BGS_FAINT_HIP']
    data['SV2_BGS_TARGET'][is_bgs_main] = sv2_targetmask.bgs_mask['BGS_BRIGHT']
    
    data = data[~(~is_bgs & was_bgs)] # exclude everything that was bgs before but it's not BGS anymore
    print(len(data))
    print('writing to ', output_filename)
    data.write(output_filename, overwrite=True)
    return output_filename

    
 
limits = {'min_ra':160, 'max_ra':200, 'min_dec':45, 'max_dec':60}

tile_file = cut_tiles("7pass-tiles.fits", tile_path="./inputs", cut_name="one_pct", limits=limits)
tile_file = cut_tiles("5pass-tiles.fits", tile_path="./inputs", cut_name="one_pct", limits=limits)


mtl_file_bright = write_onepct_mtl(output_path='./inputs/', program='bright', survey='sv2', limits=limits)
updated_mtl_file_bright = update_bgs(mtl_file_bright)

mtl_file_dark = write_onepct_mtl(output_path='./inputs/', program='dark', survey='sv2', limits=limits)
updated_mtl_file_dark = update_onepct_mtl(mtl_file_dark, mask_name='SV2_DESI_TARGET')

sky_file = write_sky_file(output_path='./inputs/', limits=limits)
