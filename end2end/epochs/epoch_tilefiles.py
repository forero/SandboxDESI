import numpy as np
from astropy.table import Table
import desimodel.io

def write_tile_file():
    desi_tiles = desimodel.io.load_tiles()
    epochs = list(set(desi_tiles['PASS']))
    min_dec = -4.0
    max_dec = 1.0
    min_ra = 207.0
    max_ra = 211.0


    for epoch in epochs:
        epoch_name = 'epoch{}.txt'.format(epoch)
        epoch_file = open(epoch_name, 'w')
        ii = desi_tiles['PASS'] == epoch
        ii &= desi_tiles['RA']<=max_ra
        ii &= desi_tiles['RA']>=min_ra
        ii &= desi_tiles['DEC']<=max_dec
        ii &= desi_tiles['DEC']>=min_dec
        ii &= desi_tiles['IN_DESI']==1
        ii &= desi_tiles['PROGRAM']=='BRIGHT'

        tiles_in = desi_tiles['TILEID'][ii]
        for tile in tiles_in:
            epoch_file.write('{}\n'.format(tile))

        epoch_file.close()


write_tile_file()
