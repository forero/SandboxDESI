from astropy.io import fits
import numpy as np
filename = "/scratch1/scratchdirs/forero/decalsdesi/Targets_Tile_000096.fits"
hdu=fits.open(filename)
print hdu.info()
table = hdu[0]
print np.shape(table)

ra = hdu[1].data['RA']
nobs = hdu[1].data['NOBS']
objtype = hdu[1].data['OBJTYPE']
prior = hdu[1].data['PRIORITY']

zero_nobs = np.where(nobs==0)
zero_prior = np.where(prior==0)


print objtype[zero_nobs]
print objtype[zero_prior]
