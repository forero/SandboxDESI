from astropy.table import Table
from desitarget.targetmask import desi_mask, bgs_mask, mws_mask
import numpy as np
import os

main_path = "/global/cscratch1/sd/forero/DR5FiberAssign/"
main_path = "/Users/forero/github/SandboxDESI/decals/"
truth = Table.read(os.path.join(main_path, 'targets', 'truth.fits'))
mtl = Table.read(os.path.join(main_path, 'targets', 'mtl.fits'))
zcat = Table.read(os.path.join(main_path, 'zcat', 'zcat.fits'))


isbgs = (mtl['DESI_TARGET'] & desi_mask.mask('BGS_ANY')) != 0
islrg = (mtl['DESI_TARGET'] & desi_mask.mask('LRG')) != 0

n_in = np.count_nonzero(isbgs|islrg)
print('total number of points in {}'.format(n_in))

print('initializing small truth')
small_truth = mtl[['TARGETID','RA','DEC']][isbgs|islrg]
small_truth['TEMPLATETYPE'] = truth['TEMPLATETYPE'][isbgs|islrg]
small_truth['NUMOBS'] = np.zeros(n_in, dtype=int)

print('making small zcat')
ii = np.in1d(zcat['TARGETID'], small_truth['TARGETID'])
small_zcat = zcat['TARGETID', 'NUMOBS'][ii]

print('checking integrity')
ii = np.in1d(small_truth['TARGETID'], small_zcat['TARGETID'])
if not (small_truth['TARGETID'][ii] == small_zcat['TARGETID']).all():
    print('We have problems with the IDs')

print('adding numobs')
small_truth['NUMOBS'][ii] = small_zcat['NUMOBS']

print('writing small catalog')
small_truth.write('bgs_lrg_fiberassign.fits', overwrite=True)
print('done')
