# testing this PR https://github.com/desihub/fiberassign/pull/24
# @home on the login node at Edison
# executed line by line on IPython

import numpy as np
from fiberassign.mock import rdzipn2targets
from desitarget.targets import desi_mask
import desitarget.mtl

targets, truth = rdzipn2targets('/project/projectdirs/desi/mocks/preliminary/objects_ss_sf0.rdzipn')

print 'targets.colnames = ', targets.colnames
print 'truth.colnames = ', truth.colnames

iisky = (targets['DESI_TARGET'] & desi_mask.SKY) != 0
iistd = (targets['DESI_TARGET'] & desi_mask.STD_FSTAR) != 0
iiobj = (~iisky & ~iistd)
print np.count_nonzero(iisky), np.count_nonzero(iistd), np.count_nonzero(iiobj)

targets[iiobj].write('targets.fits', overwrite=True)
targets[iisky].write('sky.fits', overwrite=True)
targets[iistd].write('stdstars.fits', overwrite=True)
truth[iiobj].write('truth.fits', overwrite=True)

# this part tests another PR https://github.com/desihub/desitarget/pull/32
mtl = desitarget.mtl.make_mtl(targets)
mtl.write('mtl.fits', overwrite=True)

! cp *.fits /project/projectdirs/desi/users/forero/mtl

# this now tests another PR https://github.com/desihub/fiberassign/pull/24
# I had to go first into fiberassign to run make && make install 
! ./fiberassign/bin/./fiberassign fa_features.txt

#find the tiles
from glob import glob
tiledir = '/project/projectdirs/desi/users/forero/fiberassign'
tilefiles = sorted(glob(tiledir+'/tile*.fits'))
len(tilefiles)

# this ugly hack avoids import from desi stack
import os
os.chdir('/global/homes/f/forero/desisim/py')
from desisim.quickcat import quickcat
zcat = quickcat(tilefiles, targets, truth, zcat=None, perfect=False)

#zcat.write('zcat.fits', overwrite=True)
