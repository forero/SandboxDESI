from desitarget.mock.sky import random_sky
from desitarget import desi_mask, bgs_mask, mws_mask, obsmask, obsconditions
import numpy as np
import desimodel.footprint
from astropy.table import Table

skyra, skydec = random_sky(nside=4096)
n_p = len(skyra)

data = Table()
data['RA'] = skyra
data['DEC'] = skydec
data['TARGETID'] = np.int_(1E10+ np.arange(n_p))
data['DESI_TARGET'] = np.int_(np.ones(n_p) * desi_mask['SKY'])
data['MWS_TARGET'] = np.int_(np.zeros(n_p))
data['BGS_TARGET'] = np.int_(np.zeros(n_p))
data['OBSCONDITIONS'] = np.int_(np.ones(n_p)*(obsconditions['DARK']|obsconditions['BRIGHT']|obsconditions['GRAY']))
data['BRICKNAME'] = np.chararray(n_p, itemsize=8)
data['BRICKNAME'][:] = "b0000000"
data['SUBPRIORITY'] = np.random.random(n_p)
data.write('dense_sky.fits', overwrite=True)
