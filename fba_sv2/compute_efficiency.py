from astropy.table import Table
import numpy as np

def print_eff(filename, limits={}):
       
    min_ra = limits['min_ra'] 
    max_ra = limits['max_ra'] 
    min_dec = limits['min_dec'] 
    max_dec = limits['max_dec'] 
    sv1_data = Table.read(filename)

    is_in = (sv1_data['RA']>min_ra)
    is_in = is_in&(sv1_data['RA']<max_ra)
    is_in = is_in&(sv1_data['DEC']>min_dec)
    is_in = is_in&(sv1_data['DEC']<max_dec)
    #is_avail = sv1_data['NAVAIL_FIBER']>2
    is_obs = sv1_data['NUMOBS']!=0
    is_bgs = sv1_data['isBGS_ANY']==True
    is_mws = sv1_data['isMWS_ANY']==True
    is_elg = 
    
    targets = {'BGS':'isBGS_ANY', 'MWS':'isMWS_ANY'}
    
    for i in targets.keys():
        is_target = sv1_data[targets[i]]

        n_target = np.count_nonzero(is_in&is_obs&is_target)
        eff_target = np.count_nonzero(is_in&is_obs&is_target)/np.count_nonzero(is_in&is_target)
        print('Observed {} targets: {}k\t Fiber efficiency: {:.2f}'.format(i, n_target//1000, eff_target))

    

print()
print('MAIN SELECTION - PERFECT FOCAL PLANE')
print_eff('fba_summary_bright_main.fits')