import fitsio
import numpy as np
import matplotlib.pyplot as plt
import os
import desientropy.compute

plt.style.use('astroandes.mplstyle')
os.environ['PATH'] = '/global/common/sw/cray/sles15/x86_64/texlive/live/gcc/8.2.0/tiozj27/bin/x86_64-linux/:{}'.format(os.environ['PATH'])

tile_file = "/global/cfs/cdirs/desi/spectro/redux/daily/tiles/cumulative/26056/20220221/redrock-2-26056-thru20220221.fits"
z_tile_per_exp = fitsio.read(tile_file, ext="REDSHIFTS")
ii = z_tile_per_exp['ZWARN']==0
good_z = z_tile_per_exp['Z'][ii]
n_z = np.array(len(good_z))
h = desientropy.compute.entropy_1d(z_tile_per_exp['Z'][ii])

plt.figure()
plt.scatter(np.arange(n_z), good_z, alpha=0.5)
plt.ylim([0,0.7])
plt.xlabel("Fiber Index")
plt.ylabel("Redshift")
plt.title("Petal 2 - Entropy= {:.3f} ".format(h))
plt.savefig("high_entropy_rr_example.pdf")


tile_file = "/global/cfs/cdirs/desi/spectro/redux/daily/tiles/cumulative/26056/20220221/redrock-1-26056-thru20220221.fits"
z_tile_per_exp = fitsio.read(tile_file, ext="REDSHIFTS")
ii = z_tile_per_exp['ZWARN']==0
good_z = z_tile_per_exp['Z'][ii]
n_z = np.array(len(good_z))
h = desientropy.compute.entropy_1d(z_tile_per_exp['Z'][ii])

plt.figure()
plt.scatter(np.arange(n_z), good_z, alpha=0.5)
plt.ylim([0,0.7])
plt.xlabel("Fiber Index")
plt.ylabel("Redshift")
plt.title("Petal 1 - Entropy= {:.3f} ".format(h))
plt.savefig("low_entropy_rr_example.pdf")

