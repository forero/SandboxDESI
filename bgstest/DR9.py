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

def cut_tiles(tile_path="./", cut_name="one_pct", limits={}):
        # Create output directory
    os.makedirs(tile_path, exist_ok=True)
    
    tiles = Table(desimodel.io.load_tiles())
    ii_bright = tiles['PROGRAM'] == 'BRIGHT'
    
    
    min_ra = limits['min_ra'] 
    max_ra = limits['max_ra'] 
    min_dec = limits['min_dec'] 
    max_dec = limits['max_dec'] 
    
    cut_tilefile = os.path.join(tile_path, "tiles_{}_bright.fits".format(cut_name))
    ii = (tiles['RA']>(min_ra)) & (tiles['RA']<(max_ra)) & (tiles['DEC']<max_dec) & (tiles['DEC']>min_dec) 
    ii = ii & ii_bright
    tiles[ii].write(cut_tilefile, overwrite='True')
    print("Wrote tiles to {}".format(cut_tilefile))
    
    cut_tilefile = os.path.join(tile_path, "tiles_{}_dark.fits".format(cut_name))
    ii = (tiles['RA']>min_ra) & (tiles['RA']<max_ra) & (tiles['DEC']<max_dec) & (tiles['DEC']>min_dec)
    ii = ii & (~ii_bright)
    tiles[ii].write(cut_tilefile, overwrite='True')
    print("Wrote tiles to {}".format(cut_tilefile))

    return

    

def write_gfa_file(output_path="./"):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    gfa_file = os.path.join(output_path, "gfa_onepct.fits")

    if os.path.exists(gfa_file):
        print("File {} already exist".format(gfa_file))
        return
    
    
    # List all the fits files to read
    path_to_targets = '/global/cfs/projectdirs/desi/target/catalogs/dr9/0.49.0/gfas/'
    target_files = glob.glob(os.path.join(path_to_targets, "gfas-*.fits"))
    print('gfa files to read:', len(target_files))
    target_files.sort()
    
    # Read the first file, only the columns that are useful for MTL
    data = fitsio.FITS(target_files[0], 'r')
    target_data = data[1].read()
    data.close()
    
    # Read all the other files
    for i, i_name in enumerate(target_files[1:]): 
        data = fitsio.FITS(i_name, 'r')
        tmp_data = data[1].read()
        ii_one_pct = (tmp_data['RA']>170) & (tmp_data['RA']<190) & (tmp_data['DEC']>20) & (tmp_data['DEC']<40) 
        if np.count_nonzero(ii_one_pct):
            target_data = np.hstack((target_data, tmp_data))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data), np.count_nonzero(ii_one_pct))

    target_data = Table(target_data)
    ii_one_pct = (target_data['RA']>170) & (target_data['RA']<190) & (target_data['DEC']>20) & (target_data['DEC']<40) 
    

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    print("Writing onepct gfa")
    target_data[ii_one_pct].write(gfa_file, overwrite=True)
    print("Wrote output to {}".format(gfa_file))
   
    return 
    
def write_sky_file(output_path="./"):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    sky_file = os.path.join(output_path, "sky_onepct.fits")

    if os.path.exists(sky_file):
        print("Files {} already exist".format(sky_file))
        return
    
    
    # List all the fits files to read
    path_to_targets = '/global/cfs/projectdirs/desi/target/catalogs/dr9/0.49.0/skies/'
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
        ii_one_pct = (tmp_data['RA']>170) & (tmp_data['RA']<190) & (tmp_data['DEC']>20) & (tmp_data['DEC']<40) 
        if np.count_nonzero(ii_one_pct):
            target_data = np.hstack((target_data, tmp_data))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data), np.count_nonzero(ii_one_pct))

    target_data = Table(target_data)
    ii_one_pct = (target_data['RA']>170) & (target_data['RA']<190) & (target_data['DEC']>20) & (target_data['DEC']<40) 
    

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    print("Writing onepct sky")
    target_data[ii_one_pct].write(sky_file, overwrite=True)
    print("Wrote output to {}".format(sky_file))
   
    return 


def write_onepct_mtl(output_path="./", program='bright', survey='main'):
    full_mtl_file = os.path.join(output_path, "mtl_{}_{}_onepct.fits".format(program, survey))
    
    if os.path.exists(full_mtl_file):
        print("Files {} already exist".format(full_mtl_file))
        return

    # List all the fits files to read
    path_to_targets = '/global/cfs/cdirs/desi/target/catalogs/dr9/0.49.0/targets/' + survey +'/resolve/'+program+'/'
    target_files = glob.glob(os.path.join(path_to_targets, "*targets*fits"))
    print('target files to read:', len(target_files))
    target_files.sort()
    
    #columns = ['TARGETID', 'DESI_TARGET', 'MWS_TARGET', 'BGS_TARGET', 'SUBPRIORITY', 'NUMOBS_INIT', 'PRIORITY_INIT', 'RA', 'DEC', 'HPXPIXEL', 'BRICKNAME', 'FLUX_R', 'MW_TRANSMISSION_R']
    
    # Read the first file, only the columns that are useful for MTL
    data = fitsio.FITS(target_files[0], 'r')
    target_data = data[1].read()
    data.close()
    
    # Read all the other files
    for i, i_name in enumerate(target_files[1:]): 
        data = fitsio.FITS(i_name, 'r')
        tmp_data = data[1].read()
        ii_one_pct = (tmp_data['RA']>170) & (tmp_data['RA']<190) & (tmp_data['DEC']>20) & (tmp_data['DEC']<40) 
        if np.count_nonzero(ii_one_pct):
            target_data = np.hstack((target_data, tmp_data[ii_one_pct]))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data), np.count_nonzero(ii_one_pct))
    full_mtl = desitarget.mtl.make_mtl(target_data, 'DARK|GRAY|BRIGHT')

    ii_one_pct = (full_mtl['RA']>170) & (full_mtl['RA']<190) & (full_mtl['DEC']>20) & (full_mtl['DEC']<40) 

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    print("Writing {} full".format(program))
    full_mtl[ii_one_pct].write(full_mtl_file, overwrite=True)
    print("Wrote output to {}".format(full_mtl_file))
    
    return 

def update_onepct_mtl(filename):
    data = Table.read(filename)
    print('finished reading', filename)
    isqso = (data['DESI_TARGET']&desi_mask['QSO'])!=0
    r = np.random.random(len(data))
    rr = r<0.82
    data['NUMOBS_INIT'][rr & isqso] = 1
    data['NUMOBS_MORE'][rr & isqso] = 1
    data.write(filename, overwrite=True)
    print('finished writing', filename)
    
write_onepct_mtl(output_path='./targets/', program='bright', survey='sv1')
write_onepct_mtl(output_path='./targets/', program='bright', survey='main')
write_sky_file(output_path='./targets/')
#write_gfa_file(output_path='./targets/')
#update_onepct_mtl("./targets/mtl_dark_onepct.fits")