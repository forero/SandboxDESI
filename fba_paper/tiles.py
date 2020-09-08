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


def split_tiles(output_path="./"):
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    tiles = Table(desimodel.io.load_tiles())
    
    ii_bright = tiles['PROGRAM'] == 'BRIGHT'
    ii_north = (tiles['RA']>85) & (tiles['RA']<300) & (tiles['DEC']>-15)
    
    tilefile = os.path.join(output_path, "tiles_bright_north.fits")
    if not os.path.exists(tilefile):
        tiles[ii_bright & ii_north].write(tilefile, overwrite='True')
        print("Wrote tiles to {}".format(tilefile))
    
    tilefile = os.path.join(output_path, "tiles_bright_south.fits")
    if not os.path.exists(tilefile):
        tiles[ii_bright & ~ii_north].write(tilefile, overwrite='True')
        print("Wrote tiles to {}".format(tilefile))
    
    tilefile = os.path.join(output_path, "tiles_dark_north.fits")
    if not os.path.exists(tilefile):
        tiles[~ii_bright & ii_north].write(tilefile, overwrite='True')
        print("Wrote tiles to {}".format(tilefile))
    
    tilefile = os.path.join(output_path, "tiles_dark_south.fits")
    if not os.path.exists(tilefile):
        tiles[~ii_bright & ~ii_north].write(tilefile, overwrite='True')
        print("Wrote tiles to {}".format(tilefile))
    return 