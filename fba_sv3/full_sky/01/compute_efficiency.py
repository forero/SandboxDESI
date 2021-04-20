from astropy.table import Table
import numpy as np

def print_eff(filename, limits={}):
    sv1_data = Table.read(filename)
    is_in = sv1_data['NAVAIL_FIBER']>0
    area = 14000.0
    if limits is not None:
        min_ra = limits['min_ra'] 
        max_ra = limits['max_ra'] 
        min_dec = limits['min_dec'] 
        max_dec = limits['max_dec'] 
        area = (180./np.pi) * (max_ra - min_ra) * (np.sin(np.deg2rad(max_dec)) - np.sin(np.deg2rad(min_dec)))
        
        is_in = is_in&(sv1_data['RA']>min_ra)
        is_in = is_in&(sv1_data['RA']<max_ra)
        is_in = is_in&(sv1_data['DEC']>min_dec)
        is_in = is_in&(sv1_data['DEC']<max_dec)
    
    #is_avail = sv1_data['NAVAIL_FIBER']>2
    is_obs = sv1_data['NUMOBS']!=0
    print('area (sqdeg) : ', np.int(area))

    targets = {'QSO':'isQSO', 'LRG':'isLRG','ELG':'isELG', 'BGS':'isBGS_ANY', 'MWS':'isMWS_ANY'}
    
    for i in targets.keys():
        is_target = sv1_data[targets[i]]==True

        n_target = np.count_nonzero(is_in&is_obs&is_target)
        eff_target = np.count_nonzero(is_in&is_obs&is_target)/np.count_nonzero(is_in&is_target)
        print('Observed {} : {}k ({:.0f} / sqdeg)\t\t Fiber efficiency: {:.2f}'.format(i, n_target//1000, n_target/area, eff_target))

    

limits = {'min_ra':153, 'max_ra':167, 'min_dec':3, 'max_dec':17}


print()
print('DARK TIME - SV3 DEFINITIONS - 20% LYA QSOS - 7 PASSES')
print_eff('summary_fba_mtl_updated_lya_0.20_full_sky_dark_sv3.fits', limits=None)

print()
print('BRIGHT TIME - SV3 DEFINITIONS - 4 PASSES')
print_eff('summary_fba_mtl_full_sky_bright_sv3.fits', limits=None)
