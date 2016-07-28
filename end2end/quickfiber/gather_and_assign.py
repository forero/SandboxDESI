"""
Gathers the results from fiberassign and uses the Targets file to run
a new iteration of fiberassignment.
"""

import glob
from astropy.table import Table
from astropy.io import fits

tile_path='/project/projectdirs/desi/users/forero/large_mock_test/standalone_fiberassign/*.fits'
tile_list = sorted(glob.glob(tile_path))

id_dict = {}
n_dict = {}
for tile_file in tile_list:
    tile_name = tile_file.split('/')[-1]
    tile_name = tile_name.strip('.fits')
    tile_id = int(tile_name.split('_')[1])
    id_dict[tile_id] =  fits.getdata(tile_file, 'POTENTIAL_ASSIGNMENTS')['POTENTIALTARGETID']
    n_dict[tile_id] = fits.getdata(tile_file, 'FIBER_ASSIGNMENTS')['NUMTARGET']
    print(tile_id)
