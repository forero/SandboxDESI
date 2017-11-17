from astropy.table import Table
from desitarget.targetmask import desi_mask, bgs_mask, mws_mask
import numpy as np
mtl = Table.read('mtl.fits')
zcat = Table.read("zcat.fits")
print("Efficiencies N_in N_out N_in/N_out")
for objtype in ['BGS_ANY', 'ELG', 'LRG', 'QSO', 'STD_FSTAR', 'STD_BRIGHT']:
    ii = (mtl['DESI_TARGET'] & desi_mask.mask(objtype)) != 0
    jj = np.in1d(mtl['TARGETID'][ii], zcat['TARGETID'])
    n_in = np.count_nonzero(ii)
    n_out = np.count_nonzero(jj)
    print('{:10} {} {} {:.2f}'.format(objtype, n_in, n_out, n_out/n_in))
