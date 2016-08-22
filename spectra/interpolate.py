import matplotlib as mpl
mpl.use('Agg')

from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt
from desisim.io import read_basis_templates


n_wanted = 5000
seed = 123
rand = np.random.RandomState(seed)

logg = rand.uniform(0.0, 5.5, n_wanted)
teff = rand.uniform(5500.0, 6500.0, n_wanted)
feh = rand.uniform(-2.5, 0.5, n_wanted)

baseflux, basewave, basemeta = read_basis_templates(objtype='STAR')
basearray  = np.array([basemeta['LOGG'], basemeta['TEFF'], basemeta['FEH']])
result = griddata(basearray.T, baseflux, (logg,teff,feh), method='linear')
print(np.shape(result))

if np.size(logg)==1:
    fig = plt.figure()
    plt.plot(result)
    fig.savefig('test.png')

test_template = False
if test_template :
    n = len(basemeta)
    log_err = np.ones(n)
    for ii in range(n):
        result = griddata(basearray.T, baseflux, (basemeta['LOGG'][ii], basemeta['TEFF'][ii], basemeta['FEH'][ii]), method='linear')
        log_err[ii] = np.log10(abs((result - baseflux[ii,:]).sum() +1E-10))
        print('{} {}'.format(ii, log_err[ii]))
    
