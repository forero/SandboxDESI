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

def write_initial_mtl_files(output_path="./"):
    
    # List all the fits files to read
    path_to_targets = '/global/cfs/cdirs/desi/target/catalogs/dr8/0.31.1/targets/main/resolve/'
    target_files = glob.glob(os.path.join(path_to_targets, "targets*fits"))
    print('target files to read:', len(target_files))
    target_files.sort()
    
    # Read the first file, only the columns that are useful for MTL
    data = fitsio.FITS(target_files[0], 'r')
    target_data = data[1].read(columns=['TARGETID', 'DESI_TARGET', 'MWS_TARGET', 'BGS_TARGET', 'SUBPRIORITY', 'NUMOBS_INIT', 'PRIORITY_INIT', 'RA', 'DEC', 'HPXPIXEL', 'BRICKNAME'])
    data.close()
    
    # Read all the other files
    for i, i_name in enumerate(target_files[1:]): 
        data = fitsio.FITS(i_name, 'r')
        tmp_data = data[1].read(columns=['TARGETID', 'DESI_TARGET', 'MWS_TARGET', 'BGS_TARGET', 'SUBPRIORITY', 'NUMOBS_INIT', 'PRIORITY_INIT', 'RA', 'DEC', 'HPXPIXEL', 'BRICKNAME'])
        target_data = np.hstack((target_data, tmp_data))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data))
    full_mtl = desitarget.mtl.make_mtl(target_data, 'DARK|GRAY|BRIGHT')

    ii_mtl_dark = (full_mtl['OBSCONDITIONS'] & obsconditions.DARK)!=0
    ii_mtl_gray = (full_mtl['OBSCONDITIONS'] & obsconditions.GRAY)!=0
    ii_mtl_bright = (full_mtl['OBSCONDITIONS'] & obsconditions.BRIGHT)!=0
    ii_north = (full_mtl['RA']>85) & (full_mtl['RA']<300) & (full_mtl['DEC']>-15)

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    print("Writing DARK + GRAY NORTH cap")
    mtl_file = os.path.join(output_path, "dark_gray_north.fits")
    if os.path.exists(mtl_file):
        print("File {} already exists".format(mtl_file))
    else:
        full_mtl[(ii_mtl_dark | ii_mtl_gray) & ii_north].write(mtl_file, overwrite=True)
        print("Wrote output to {}".format(mtl_file))
    
    
    print("Writing BRIGHT NORTH cap")
    mtl_file = os.path.join(output_path, "bright_north.fits")
    if os.path.exists(mtl_file):
        print("File {} already exists".format(mtl_file))
    else:
        full_mtl[ii_mtl_bright & ii_north].write(mtl_file, overwrite=True)
        print("Wrote output to {}".format(mtl_file))
    
    print("Writing DARK + GRAY SOUTH cap")
    mtl_file = os.path.join(output_path, "dark_gray_south.fits")
    if os.path.exists(mtl_file):
        print("File {} already exists".format(mtl_file))
    else:
        full_mtl[(ii_mtl_dark | ii_mtl_gray) & ~ii_north].write(mtl_file, overwrite=True)
        print("Wrote output to {}".format(mtl_file))
    
    print("Writing BRIGHT SOUTH cap")
    mtl_file = os.path.join(output_path, "bright_south.fits")
    if os.path.exists(mtl_file):
        print("File {} already exists".format(mtl_file))
    else:
        full_mtl[ii_mtl_bright & ~ii_north].write(mtl_file, overwrite=True)
        print("Wrote output to {}".format(mtl_file))

def split_sky(output_path="./"):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    sky_data = Table.read("/global/cfs/cdirs/desi/target/catalogs/dr8/0.31.0/skies/skies-dr8-0.31.0.fits")
    ii_north = (sky_data['RA']>85) & (sky_data['RA']<300) & (sky_data['DEC']>-15)

    sky_file = os.path.join(output_path, "sky_north.fits")
    if os.path.exists(sky_file):
        print("File {} already exists".format(mtl_file))
    else:
        sky_data[ii_north].write(sky_file, overwrite=True)
        print("Wrote output to {}".format(sky_file))
        
    sky_file = os.path.join(output_path, "sky_south.fits")
    if os.path.exists(sky_file):
        print("File {} already exists".format(mtl_file))
    else:
        sky_data[~ii_north].write(sky_file, overwrite=True)
        print("Wrote output to {}".format(sky_file))

def split_tiles(output_path="./"):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    tiles = Table(desimodel.io.load_tiles())
    
    ii_bright = tiles['PROGRAM'] == 'BRIGHT'
    ii_north = (tiles['RA']>85) & (tiles['RA']<300) & (tiles['DEC']>-15)
    
    tilefile = os.path.join(output_path, "tiles_bright_north.fits")
    tiles[ii_bright & ii_north].write(tilefile, overwrite='True')
    print("Wrote tiles to {}".format(tilefile))
    
    tilefile = os.path.join(output_path, "tiles_bright_south.fits")
    tiles[ii_bright & ~ii_north].write(tilefile, overwrite='True')
    print("Wrote tiles to {}".format(tilefile))
    
    tilefile = os.path.join(output_path, "tiles_dark_gray_north.fits")
    tiles[~ii_bright & ii_north].write(tilefile, overwrite='True')
    print("Wrote tiles to {}".format(tilefile))
    
    tilefile = os.path.join(output_path, "tiles_dark_gray_south.fits")
    tiles[~ii_bright & ~ii_north].write(tilefile, overwrite='True')
    print("Wrote tiles to {}".format(tilefile))
    
    ntiles = tiles[ii_bright & ii_north]
    tilefile = os.path.join(output_path, "tiles_test_bright_north.fits")
    ntiles[:10].write(tilefile, overwrite='True')
    print("Wrote tiles to {}".format(tilefile))
    
    ntiles = tiles[~ii_bright & ii_north]
    tilefile = os.path.join(output_path, "tiles_test_dark_north.fits")
    ntiles[:10].write(tilefile, overwrite='True')
    print("Wrote tiles to {}".format(tilefile))
    

        
targets_path = "targets"
mtl_files = {}
mtl_files['dark_gray_north']  = os.path.join(targets_path, "dark_gray_north.fits")
mtl_files['dark_gray_south']  = os.path.join(targets_path, "dark_gray_south.fits")
mtl_files['bright_north']  = os.path.join(targets_path, "bright_north.fits")
mtl_files['bright_south'] = os.path.join(targets_path, "bright_south.fits")

all_exist = True
for k in mtl_files.values():
    all_exist &= os.path.exists(k)
print(all_exist)

if not all_exist:
    write_initial_mtl_files(output_path=targets_path)
    
    
sky_files = {}
sky_files['sky_north']  = os.path.join(targets_path, "sky_north.fits")
sky_files['sky_south']  = os.path.join(targets_path, "sky_south.fits")

all_sky_exist = True
for k in sky_files.values():
    all_sky_exist &= os.path.exists(k)
print(all_sky_exist)

if not all_sky_exist:
    split_sky(output_path=targets_path)
    
split_tiles("footprint")