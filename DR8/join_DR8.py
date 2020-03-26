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

def write_initial_mtl_file(output_path="./"):
    
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
    for i, i_name in enumerate(target_files[30:]): #FIXME - should start at 1
        data = fitsio.FITS(i_name, 'r')
        tmp_data = data[1].read(columns=['TARGETID', 'DESI_TARGET', 'MWS_TARGET', 'BGS_TARGET', 'SUBPRIORITY', 'NUMOBS_INIT', 'PRIORITY_INIT', 'RA', 'DEC', 'HPXPIXEL', 'BRICKNAME'])
        target_data = np.hstack((target_data, tmp_data))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data))
    full_mtl = desitarget.mtl.make_mtl(target_data, 'DARK|GRAY|BRIGHT')

    ii_mtl_dark = (full_mtl['OBSCONDITIONS'] & obsconditions.DARK)!=0
    ii_mtl_gray = (full_mtl['OBSCONDITIONS'] & obsconditions.GRAY)!=0
    ii_north = (full_mtl['RA']>85) & (full_mtl['RA']<300) & (full_mtl['DEC']>-15)

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    print("Writing DARK + GRAY NORTH cap")
    mtl_file = os.path.join(output_path, "dark_gray_north.fits")
    full_mtl[(ii_mtl_dark | ii_mtl_gray) & ii_north].write(mtl_file, overwrite=True)
    print("Wrote output to {}".format(mtl_file))
    
    print("Writing BRIGHT NORTH cap")
    mtl_file = os.path.join(output_path, "bright_north.fits")
    full_mtl[~(ii_mtl_dark | ii_mtl_gray) & ii_north].write(mtl_file, overwrite=True)
    print("Wrote output to {}".format(mtl_file))
    
    print("Writing DARK + GRAY SOUTH cap")
    mtl_file = os.path.join(output_path, "dark_gray_south.fits")
    full_mtl[(ii_mtl_dark | ii_mtl_gray) & ~ii_north].write(mtl_file, overwrite=True)
    print("Wrote output to {}".format(mtl_file))
    
    print("Writing BRIGHT SOUTH cap")
    mtl_file = os.path.join(output_path, "bright_south.fits")
    full_mtl[~(ii_mtl_dark | ii_mtl_gray) & ~ii_north].write(mtl_file, overwrite=True)
    print("Wrote output to {}".format(mtl_file))

write_initial_mtl_file(output_path="targets")
#    print("Writing subset in the northern cap")
#    mtl_data = Table.read(mtl_file)
#    subset_ii = ra_dec_subset(mtl_data)
#    mtl_data[subset_ii].write(initial_mtl_file, overwrite=True)