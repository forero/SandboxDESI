from astropy.table import Table
import numpy as np

def print_eff(filename):
    sv1_data = Table.read(filename)

    is_in = (sv1_data['RA']>173.0)
    is_in = is_in&(sv1_data['RA']<187.0)
    is_in = is_in&(sv1_data['DEC']>23.0)
    is_in = is_in&(sv1_data['DEC']<37.0)
    #is_avail = sv1_data['NAVAIL_FIBER']>2
    is_obs = sv1_data['NUMOBS']!=0
    is_bgs = sv1_data['isBGS_ANY']==True
    is_mws = sv1_data['isMWS_ANY']==True

    n_bgs = np.count_nonzero(is_in&is_obs&is_bgs)
    eff_bgs = np.count_nonzero(is_in&is_obs&is_bgs)/np.count_nonzero(is_in&is_bgs)
    print('Observed BGS targets: {}k\t Fiber efficiency: {:.2f}'.format(n_bgs//1000, eff_bgs))

    n_mws = np.count_nonzero(is_in&is_obs&is_mws)
    eff_mws = np.count_nonzero(is_in&is_obs&is_mws)/np.count_nonzero(is_in&is_mws)
    print('Observed MWS targets: {}k\t Fiber efficiency: {:.2f}'.format(n_mws//1000, eff_mws))
    

print()
print('MAIN SELECTION - PERFECT FOCAL PLANE')
print_eff('fba_summary_bright_main.fits')
#print()
#print('SV1 SELECTION | PERFECT FOCAL PLANE')
#print_eff('fba_summary_bright_sv1.fits')


print()
print('MAIN SELECTION - REAL FOCAL PLANE')
print_eff('fba_summary_bright_main_updated_pos.fits')
print()
print('SV1 SELECTION - REAL FOCAL PLANE')
print_eff('fba_summary_bright_sv1_updated_pos.fits')


#print()
#print('NEW BGS SELECTION - PERFECT FOCAL PLANE')
#print_eff('fba_summary_bright_newbgs_sv1.fits')

print()
print('NEW BGS SELECTION (JAIME) - REAL FOCAL PLANE')
print_eff('fba_summary_bright_newbgs_sv1_updated_pos.fits')
print()
print('NEW BGS SELECTION (DAVID) - REAL FOCAL PLANE')
print_eff('fba_summary_bright_newbgs_david_sv1_updated_pos.fits')