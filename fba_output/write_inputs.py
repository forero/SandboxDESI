from astropy.table import Table
import numpy as np
import desimodel.io

a = Table.read('/global/cfs/projectdirs/desi/target/catalogs/dr8/0.42.0/targets/main/resolve/dark/targets-dark-hp-4.fits')                       
n = len(a)
r = np.random.random(n)
a[r<0.01].write('inputs/targets.fits')

min_ra, max_ra, min_dec, max_dec = np.min(a['RA']), np.max(a['RA'])  , np.min(a['DEC']), np.max(a['DEC'])                                                    
tiles = desimodel.io.load_tiles() 
ii = (tiles['RA']>min_ra) & (tiles['RA']<max_ra) & (tiles['DEC']>min_dec) & (tiles['DEC']<max_dec) & (tiles['PROGRAM']=='DARK')  & (tiles['PASS']==1) 

tiles_subset = tiles[ii]  
Table(tiles_subset[:10]).write('inputs/tiles_subset.fits')  

sky = Table.read('/global/cfs/projectdirs/desi/target/catalogs/dr8/0.39.0/skies/skies-dr8-hp-4.fits')
n = len(sky)
r = np.random.random(n)
sky[r<0.01].write('inputs/sky.fits')