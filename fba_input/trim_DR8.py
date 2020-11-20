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


def write_sky_files(output_path="./"):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)

        
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
    for i, i_name in enumerate(target_files[1:2]): 
        data = fitsio.FITS(i_name, 'r')
        tmp_data = data[1].read()
        target_data = np.hstack((target_data, tmp_data))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data))

    target_data = Table(target_data)
    target_data.write("full_sky.fits")
    return


def write_initial_mtl_files(output_path="./", program='bright'):
    north_mtl_file = os.path.join(output_path, "{}_north.fits".format(program))
    south_mtl_file = os.path.join(output_path, "{}_south.fits".format(program))

    if os.path.exists(north_mtl_file) and os.path.exists(south_mtl_file):
        print("Files {} {} already exist".format(north_mtl_file, south_mtl_file))
        return

    # List all the fits files to read
    path_to_targets = '/global/cfs/projectdirs/desi/target/catalogs/dr8/0.42.0/targets/main/resolve/'+program+'/'
    target_files = glob.glob(os.path.join(path_to_targets, "targets*fits"))
    print('target files to read:', len(target_files))
    target_files.sort()
    
    columns = ['TARGETID', 'DESI_TARGET', 'MWS_TARGET', 'BGS_TARGET', 'SUBPRIORITY', 
               'NUMOBS_INIT', 'PRIORITY_INIT', 'RA', 'DEC', 'HPXPIXEL', 'BRICKNAME', 
               'FLUX_G', 'FLUX_R', 'FLUX_Z', 'PHOTSYS',
              'FIBERTOTFLUX_G', 'FIBERTOTFLUX_R', 'FIBERTOTFLUX_Z',
              'PARALLAX', 'PMRA', 'PMDEC', 'REF_EPOCH']
    
# not found 'PRIORITY', 'SCND_TARGET'

#SERSC,SHAPE_R,SHAPE_E1,SHAPE_E2 (or whatever the DR9 set of shape parameters are)
#PARALLAX, 
#EBV
#PRIORITY, SUBPRIORITY, OBSPRIORITY, NUMOBS_MORE
#FLUX_IVAR_G, FLUX_IVAR_R, FLUX_IVAR_Z
#FIBERFLUX_G, FIBERFLUX_R, FIBERFLUX_Z
#Maybe: WISE_W1, WISE_W2
#Maybe: REF_ID, REF_CAT
#Maybe: GAIA_PHOT_G_MEAN_MAG, GAIA_PHOT_BP_MEAN_MAG, GAIA_PHOT_BR_MEAN_MAG]
    
    # Read the first file, only the columns that are useful for MTL
    data = fitsio.FITS(target_files[0], 'r')
    target_data = data[1].read(columns=columns)
    data.close()
    
    # Read all the other files
    for i, i_name in enumerate(target_files[1:2]): 
        data = fitsio.FITS(i_name, 'r')
        tmp_data = data[1].read(columns=columns)
        target_data = np.hstack((target_data, tmp_data))
        data.close()
        print('reading file', i, len(target_files), len(tmp_data))
    #full_mtl = desitarget.mtl.make_mtl(target_data, 'DARK|GRAY|BRIGHT')
    
    Table(target_data).write('full_mtl_{}.fits'.format(program), overwrite=True)

    return

#87 MB
write_initial_mtl_files(output_path="./", program='bright')