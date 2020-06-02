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

def cut_mtl_sky_tiles(output_path="./", tile_path="./"):
    cut_mtl_dark_file = os.path.join(output_path, "cut_dark_north.fits")
    cut_mtl_bright_file = os.path.join(output_path, "cut_dark_bright.fits")
    cut_sky_file = os.path.join(output_path, "cut_sky_north.fits")
    
    if os.path.exists(cut_mtl_file) and os.path.exists(cut_sky_file) and os.path.exists(cut_mtl_bright_file):
        return
    
    filename = os.path.join(output_path, "dark_north.fits")
    filein = fitsio.FITS(filename)
    mtl_data = filein[1].read()
    ii = (mtl_data['RA']>150) & (mtl_data['RA']<200) & (mtl_data['DEC']<10) & (mtl_data['DEC']>-10)
    cut_mtl = Table(mtl_data[ii]).write(cut_mtl_dark_file, overwrite=True)
    
    filename = os.path.join(output_path, "bright_north.fits")
    filein = fitsio.FITS(filename)
    mtl_data = filein[1].read()
    ii = (mtl_data['RA']>150) & (mtl_data['RA']<200) & (mtl_data['DEC']<10) & (mtl_data['DEC']>-10)
    cut_mtl = Table(mtl_data[ii]).write(cut_mtl_bright_file, overwrite=True)

    north_sky_file = os.path.join(output_path, "sky_north.fits")
    filein = fitsio.FITS(north_sky_file)
    sky_data = filein[1].read()
    ii = (sky_data['RA']>150) & (sky_data['RA']<200) & (sky_data['DEC']<10) & (sky_data['DEC']>-10)
    cut_sky = Table(sky_data[ii]).write(cut_sky_file, overwrite=True)
    
    tilefile = os.path.join(tile_path, "tiles_bright_north.fits")
    cut_tilefile = os.path.join(tile_path, "tiles_cut_bright_north.fits")
    tiles = Table.read(tilefile)
    ii = (tiles['RA']>105) & (tiles['RA']<195) & (tiles['DEC']<5) & (tiles['DEC']>-5)
    tiles[ii].write(cut_tilefile, overwrite='True')
    print("Wrote tiles to {}".format(cut_tilefile))
    
    tilefile = os.path.join(tile_path, "tiles_dark_north.fits")
    cut_tilefile = os.path.join(tile_path, "tiles_cut_dark_north.fits")
    tiles = Table.read(tilefile)
    ii = (tiles['RA']>105) & (tiles['RA']<195) & (tiles['DEC']<5) & (tiles['DEC']>-5)
    tiles[ii].write(cut_tilefile, overwrite='True')
    print("Wrote tiles to {}".format(cut_tilefile))
    
    
def write_initial_mtl_files(output_path="./", program='bright'):
    north_mtl_file = os.path.join(output_path, "{}_north.fits".format(program))
    south_mtl_file = os.path.join(output_path, "{}_south.fits".format(program))

    if os.path.exists(north_mtl_file) or os.path.exists(south_mtl_file):
        print("Files {} {} already exist".format(north_mtl_file, south_mtl_file))
        return

    # List all the fits files to read
    path_to_targets = '/global/cfs/projectdirs/desi/target/catalogs/dr8/0.39.0/targets/main/resolve/'+program+'/'
    target_files = glob.glob(os.path.join(path_to_targets, "targets*fits"))
    print('target files to read:', len(target_files))
    target_files.sort()
    
    columns = ['TARGETID', 'DESI_TARGET', 'MWS_TARGET', 'BGS_TARGET', 'SUBPRIORITY', 'NUMOBS_INIT', 'PRIORITY_INIT', 'RA', 'DEC', 'HPXPIXEL', 'BRICKNAME', 'FLUX_R', 'MW_TRANSMISSION_R']
    
    # Read the first file, only the columns that are useful for MTL
    data = fitsio.FITS(target_files[0], 'r')
    target_data = data[1].read(columns=columns)
    data.close()
    
    # Read all the other files
    for i, i_name in enumerate(target_files[1:]): 
        data = fitsio.FITS(i_name, 'r')
        tmp_data = data[1].read(columns=columns)
        target_data = np.hstack((target_data, tmp_data))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data))
    full_mtl = desitarget.mtl.make_mtl(target_data, 'DARK|GRAY|BRIGHT')

    ii_north = (full_mtl['RA']>85) & (full_mtl['RA']<300) & (full_mtl['DEC']>-15)

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    print("Writing {} north cap".format(program))
    full_mtl[ii_north].write(north_mtl_file, overwrite=True)
    print("Wrote output to {}".format(north_mtl_file))
        
    print("Writing {} south cap".format(program))
    full_mtl[~ii_north].write(south_mtl_file, overwrite=True)
    print("Wrote output to {}".format(south_mtl_file))
    return 

def write_sky_files(output_path="./"):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    north_sky_file = os.path.join(output_path, "sky_north.fits")
    south_sky_file = os.path.join(output_path, "sky_south.fits")

    if os.path.exists(north_sky_file) or os.path.exists(south_sky_file):
        print("Files {} {} already exist".format(north_sky_file, south_sky_file))
        return
    
    
    # List all the fits files to read
    path_to_targets = '/global/cfs/projectdirs/desi/target/catalogs/dr8/0.39.0/skies/'
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
        target_data = np.hstack((target_data, tmp_data))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data))

    target_data = Table(target_data)
    ii_north = (target_data['RA']>85) & (target_data['RA']<300) & (target_data['DEC']>-15)

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    print("Writing north sky cap")
    target_data[ii_north].write(north_sky_file, overwrite=True)
    print("Wrote output to {}".format(north_sky_file))
        
    print("Writing south sky cap")
    target_data[~ii_north].write(south_sky_file, overwrite=True)
    print("Wrote output to {}".format(south_sky_file))
    return 


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
    
    tilefile = os.path.join(output_path, "tiles_dark_north.fits")
    tiles[~ii_bright & ii_north].write(tilefile, overwrite='True')
    print("Wrote tiles to {}".format(tilefile))
    
    tilefile = os.path.join(output_path, "tiles_dark_south.fits")
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
write_initial_mtl_files(output_path=targets_path, program="dark")
write_initial_mtl_files(output_path=targets_path, program="bright")
write_sky_files(output_path=targets_path)
split_tiles("footprint")
cut_mtl_sky_tiles(output_path=targets_path, tile_path="footprint")