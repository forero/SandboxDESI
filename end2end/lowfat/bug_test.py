import numpy as np
import desitarget.mtl
from astropy.table import Table, Column
import os.path
import os

epoch_path = "/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/"
targets_path = "/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/"
output_path =  "/project/projectdirs/desi/users/forero/lowfat_perfect/"

print(os.path.join(output_path, '1/zcat.fits'))
zcat = Table.read(os.path.join(output_path, '1/zcat.fits'), format='fits')
targets = Table.read(os.path.join(targets_path,'targets.fits'))

mtl = desitarget.mtl.make_mtl(targets, zcat, trim=True)
mtl.write('a.fits', overwrite=True)
mtl_test = Table.read('a.fits') 
iielg = mtl_test['DESI_TARGET'] == 2
print(mtl_test['NUMOBS_MORE'][iielg])

mtl = desitarget.mtl.make_mtl(targets, zcat, trim=False)
mtl.write('b.fits', overwrite=True)
mtl_test = Table.read('b.fits') 
iielg = mtl_test['DESI_TARGET'] == 2
print(mtl_test['NUMOBS_MORE'][iielg])

os.remove('a.fits')
os.remove('b.fits')
