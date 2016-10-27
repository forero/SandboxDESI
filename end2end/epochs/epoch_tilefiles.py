import numpy as np
from astropy.table import Table

def write_tile_file(desitiles="desi-tiles.par", epochtiles="lowfat-desi-tiles.par"):
    desi_tiles = Table.read(desitiles)
    epochs = list(set(desi_tiles['PASS']))
    

    for epoch in epochs:
        epoch_name = 'epoch{}.dat'.format(epoch)
        epoch_file = open(epoch_name, 'w')
        ii = desi_tiles['PASS'] == epoch
        ii &= desi_tiles['RA']<30.0
        ii &= desi_tiles['DEC']<20.0
        ii &= desi_tiles['DEC']>0

        tiles_in = desi_tiles['TILEID'][ii]
        for tile in tiles_in:
            epoch_file.write('{}\n'.format(tile))

        epoch_file.close()

desitiles = "/project/projectdirs/desi/software/edison/desimodel/0.4.5/data/footprint/desi-tiles.fits"
write_tile_file(desitiles=desitiles)
