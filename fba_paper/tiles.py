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

def tiles_into_passes(input_tiles="tiles.fits", input_path="./",output_path="./"):
    tiles = Table.read(os.path.join(input_path, input_tiles))
    passes = set(tiles['PASS'])
    
    for p in passes:
        filename = input_tiles.replace(".fits", "_pass_{}.fits".format(p))
        filename = os.path.join(output_path, filename)
        new_tiles = tiles[tiles['PASS']==p]
        new_tiles.write(filename, overwrite=True)
        print(filename)


def tiles_into_cumulative_passes(input_tiles="tiles.fits", input_path="./",output_path="./"):
    tiles = Table.read(os.path.join(input_path, input_tiles))
    passes = np.sort(np.array(list(set(tiles['PASS']))))
    print(passes)
    
    for p in passes:
        filename = input_tiles.replace(".fits", "_up_to_pass_{}.fits".format(p))
        filename = os.path.join(output_path, filename)
        new_tiles = tiles[tiles['PASS']==p]
        for l in passes:
            if l < p:
                new_tiles = vstack([new_tiles, tiles[tiles['PASS']==l]])
        print(p, len(new_tiles))
        new_tiles.write(filename, overwrite=True)
        print(filename)        

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
