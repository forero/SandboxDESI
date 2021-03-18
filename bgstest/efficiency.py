from astropy.table import Table
import numpy as np

def print_eff(filename):
    sv1_data = Table.read(filename)

    is_avail = sv1_data['NAVAIL_FIBER']>2
    is_obs = sv1_data['NUMOBS']!=0
    is_bgs = sv1_data['isBGS_ANY']==True
    is_mws = sv1_data['isMWS_ANY']==True

    n_bgs = np.count_nonzero(is_avail&is_obs&is_bgs)
    eff_bgs = np.count_nonzero(is_avail&is_obs&is_bgs)/np.count_nonzero(is_avail&is_bgs)
    print('Observed BGS targets: {}k\t Fiber efficiency: {:.2f}'.format(n_bgs//1000, eff_bgs))

    n_mws = np.count_nonzero(is_avail&is_obs&is_mws)
    eff_mws = np.count_nonzero(is_avail&is_obs&is_mws)/np.count_nonzero(is_avail&is_mws)
    print('Observed MWS targets: {}k\t Fiber efficiency: {:.2f}'.format(n_mws//1000, eff_mws))
    

print()
print('MAIN SELECTION')
print_eff('fba_summary_bright_main.fits')
print()
print('SV1 SELECTION')
print_eff('fba_summary_bright_sv1.fits')