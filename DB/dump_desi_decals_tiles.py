import psycopg2
import sys
import numpy as np
import fitsio as F
import test_targetting as tt
from astropy.io import fits
import os
import multiprocessing

def get_tiles():
    """
    input: none
    output: numpy array with RA, DEC, PASS footprint information from desi-tiles.fits
    """
    tiling_file = os.path.join(os.environ['DESIMODEL'], 'data/footprint/', 'desi-tiles.fits')
    try:
        dat = F.read(tiling_file,columns=('RA','DEC','PASS','IN_DESI', 'TILEID'))
        ww  = np.nonzero( dat['IN_DESI'] )[0]
        ra_desi  = (dat[  'RA'][ww]).astype('f4')
        dec_desi  = (dat[ 'DEC'][ww]).astype('f4')
        pass_desi = (dat[ 'PASS'][ww]).astype('int')
        tileid_desi = (dat[ 'TILEID'][ww]).astype('int')
    except Exception, e:
        import traceback
        print 'ERROR in get_tiles'
        traceback.print_exc()
        raise e    
    return ra_desi, dec_desi, pass_desi, tileid_desi

ra_tiles, dec_tiles, pass_tiles, tileid = get_tiles()

id_decals = np.where((ra_tiles<360.0)&(ra_tiles>320.0)&(dec_tiles<0.5)&(dec_tiles>-0.5))
id_decals = id_decals[0]
print dec_tiles[id_decals], ra_tiles[id_decals], pass_tiles[id_decals], tileid[id_decals]

n_tiles = np.size(id_decals)
for i in range(0,n_tiles):
    ra = ra_tiles[id_decals[i]]
    dec = dec_tiles[id_decals[i]]
    radius = 1.6
    tile = tileid[id_decals[i]]    
    print "working on ra %f dec %f, item %d"%(ra,dec, i)
    tt.extract_targets(ra, dec, radius, tile)

