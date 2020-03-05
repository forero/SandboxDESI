"""
Simple file to reproduce issue #237 in fiberassign.


 The problem

 ICS uses Pandas dataframes to parse fiberassign tables, but Pandas doesn't support 2D columns. 
 When merging the target catalog into the FIBERASSIGN table, exclude 2D columns.
 Example problem at KPNO:

import fitsio
t = fitsio.read('/data/tiles/ALL_tiles/v1/fiberassign-059958.fits', 'FIBERASSIGN')
for name in t.dtype.names:
    if len(t[name].shape) > 1:
        print(name, t[name].shape)

...
DCHISQ (5000, 5)
"""

from astropy.table import Table
import desimodel.focalplane
import numpy as np
from desitarget.targetmask import desi_mask, obsconditions
import os, sys, subprocess
import fitsio

# I take as an input the results from this notebook https://github.com/desihub/tutorials/blob/c977a9213556e155bc6d9e12c01e49800035ca93/FiberAssignDECaLS.ipynb
def run_fiberassign():
    cmd = 'fiberassign --overwrite --mtl mtl.fits --sky sky.fits --footprint ./tiles.fits --outdir ./'
    print('RUNNING: '+cmd)
    try:
        results = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT)
        print(results.decode())
        print('--- SUCCESS ---')
    except subprocess.CalledProcessError as ex:
        print('--- ERROR {} ---'.format(ex.returncode))
        print(ex.output.decode())
    
def test_problem(fiberassignfile):
    t = fitsio.read(fiberassignfile, 'FIBERASSIGN')
    cols = 0
    for name in t.dtype.names:
        if len(t[name].shape) > 1:
            cols = cols+1
            print('FIBERASSIGN', name, t[name].shape)
            
    t = fitsio.read(fiberassignfile, 'TARGETS')
    for name in t.dtype.names:
        if len(t[name].shape) > 1:
            cols = cols+1
            print('TARGETS', name, t[name].shape)
    if cols==0:
        problem = False
    else:
        problem = True
    return problem


fiberfile = "fiberassign-021539.fits"

#if (not os.path.exists(fiberfile)):
run_fiberassign()

problem = test_problem(fiberfile)

if problem:
    print("We have a problem with the column sizes")
else:
    print("Problem solved")
