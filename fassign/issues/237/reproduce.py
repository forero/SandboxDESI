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

#def create_simple_targets():

def generate_random_targets(tiles, density=2400):
    #- Get basic bounds; don't worry about RA wraparound for this example
    tile_radius = desimodel.focalplane.get_tile_radius_deg()
    ramin = np.min(tiles['RA'] - tile_radius*np.cos(np.radians(tiles['DEC'])))
    ramax = np.max(tiles['RA'] + tile_radius*np.cos(np.radians(tiles['DEC'])))
    decmin = np.min(tiles['DEC']) - tile_radius
    decmax = np.max(tiles['DEC']) + tile_radius
    
    area = (ramax-ramin) * np.degrees((np.sin(np.radians(decmax)) - np.sin(np.radians(decmin))))
    n = int(area*density)

    #- Iterate if needed to get unique TARGETIDs
    while True:
        targetids = np.random.randint(0, 2**62-1, n)
        if len(set(targetids)) == n:
            break

    #- Create targets table
    targets = Table()
    targets['TARGETID'] = targetids
    targets['RA'] = np.random.uniform(ramin, ramax, n)
    phimin = np.radians(90-decmin)
    phimax = np.radians(90-decmax)
    targets['DEC'] = 90-np.degrees(np.arccos(np.random.uniform(np.cos(phimin), np.cos(phimax), n)))
    targets['DESI_TARGET'] = np.zeros(n, dtype='i8')
    targets['BGS_TARGET'] = np.zeros(n, dtype='i8')
    targets['MWS_TARGET'] = np.zeros(n, dtype='i8')
    targets['SUBPRIORITY'] = np.random.uniform(0, 1, n)
    targets['BRICKNAME'] = np.full(n, '000p0000')    #- required !?!
    targets['BRICKID'] = np.full(n, 0)    #- required !?!
    targets['BRICK_OBJID'] = np.arange(n)
    
    #- dummy values for fluxes
    for filt in ['G', 'R', 'Z']:
        targets['FIBERFLUX_'+filt] = np.zeros(n, dtype='f4')
        targets['FIBERFLUX_IVAR_'+filt] = np.ones(n, dtype='f4')
    
    #- Trim to targets that are covered by a tile
    ii = desimodel.footprint.is_point_in_desi(tiles, targets['RA'], targets['DEC'])
    targets = targets[ii]
    return targets
    
#- This is an ELG like sample
def generate_mtl(tiles):
    targets = generate_random_targets(tiles, density=2400)
    n = len(targets)
    targets['PRIORITY'] = 1000
    targets['SUBPRIORITY'] = np.random.uniform(0, 1, n)
    targets['DESI_TARGET'] = desi_mask.ELG
    targets['OBSCONDITIONS'] = np.ones(n, dtype='i4') * obsconditions.DARK
    targets['NUMOBS_MORE'] = np.ones(n, dtype='i8')
    targets.meta['EXTNAME'] = 'MTL'
    targets.write('mtl.fits', overwrite=True)
    
def generate_sky(tiles):
    fiber_density = 5000 / 7.5
    sky_density = 4*fiber_density
    sky = generate_random_targets(tiles, density=sky_density)
    nsky = len(sky)
    sky['DESI_TARGET'] = desi_mask.SKY
    sky['OBSCONDITIONS'] = np.ones(nsky, dtype='i4') * obsconditions.mask('DARK|GRAY|BRIGHT')
    sky.meta['EXTNAME'] = 'SKY'
    sky.write('sky.fits', overwrite=True)

def create_simple_tiles(ntiles=1):
    ntiles = ntiles
    tiles = Table()
    tile_radius = desimodel.focalplane.get_tile_radius_deg()
    tiles['TILEID'] = np.arange(ntiles, dtype='i4')+10
    tiles['RA'] = 2 + np.arange(ntiles)*0.5*tile_radius
    tiles['DEC'] = np.zeros(ntiles)
    tiles['PASS'] = np.zeros(ntiles, dtype='i2')
    tiles['OBSCONDITIONS'] = np.ones(ntiles, dtype='i4') * obsconditions.DARK
    tiles['IN_DESI'] = np.ones(ntiles, dtype='i2')
    tiles['PROGRAM'] = np.full(ntiles, 'DARK', dtype='S6')
    tiles.write('tiles.fits', format='fits', overwrite=True)
    return tiles
    
    
def run_fiberassign():
    cmd = 'fiberassign --overwrite --mtl mtl.fits --sky sky.fits'
    cmd += ' --footprint ./tiles.fits'
    cmd += ' --outdir ./'
    cmd = cmd.format(outdir="./")
    print('RUNNING: '+cmd)
    try:
        results = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT)
        print(results.decode())
        print('--- SUCCESS ---')
    except subprocess.CalledProcessError as ex:
        print('--- ERROR {} ---'.format(ex.returncode))
        print(ex.output.decode())
    
def test_problem():
    t = fitsio.read('fiberassign-000010.fits', 'FIBERASSIGN')
    cols = 0
    for name in t.dtype.names:
        if len(t[name].shape) > 1:
            cols = cols+1
            print(name, t[name].shape)
    if cols==0:
        problem = False
    else:
        problem = True
    return problem

tiles = create_simple_tiles()
generate_mtl(tiles)
generate_sky(tiles)
run_fiberassign()
problem = test_problem()
if problem:
    print("We have a problem with the column sizes")
else:
    print("Problem solved")
