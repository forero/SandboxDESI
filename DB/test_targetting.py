import psycopg2
import sys
import numpy as np
import fitsio as F
import os

def get_tiles():
    """
    input: none
    output: numpy array with RA, DEC, PASS footprint information from desi-tiles.fits
    """
    tiling_file = os.path.join(os.environ['DESIMODEL'], 'data/footprint/', 'desi-tiles.fits')
    try:
        dat = F.read(tiling_file,columns=('RA','DEC','PASS','IN_DESI'))
        ww  = np.nonzero( dat['IN_DESI'] )[0]
        ra_desi  = (dat[  'RA'][ww]).astype('f4')
        dec_desi  = (dat[ 'DEC'][ww]).astype('f4')
        pass_desi = (dat[ 'DEC'][ww]).astype('int')
    except Exception, e:
        import traceback
        print 'ERROR in get_tiles'
        traceback.print_exc()
        raise e    
    return ra_desi, dec_desi, pass_desi


def simple_test():
    ra = 335.0
    dec = 0.0
    radius = 0.7
    con = psycopg2.connect(host='scidb2.nersc.gov', user='desi_user', database='desi')
    cur = con.cursor()
    cur.execute("select candidate.id, candidate.ra, candidate.dec, decam.gflux, decam.rflux, decam.zflux, wise.w1flux, decam.gfracflux, decam.rfracflux, decam.zfracflux, wise.w1fracflux from  candidate, decam, wise where q3c_radial_query(candidate.ra, candidate.dec, %f, %f, %f) and decam.cand_id = candidate.id and wise.cand_id = candidate.id and decam.g_anymask=0 and decam.r_anymask =0 and decam.z_anymask=0;"%(ra,dec,radius))
    m=cur.fetchall()
    data = np.array(m)
    
    data_dic = dict([('ID', data[:,0]), ('RA', data[:,1]), ('DEC', data[:,2]), 
                     ('GFLUX', data[:,3]), ('RFLUX', data[:,4]), ('ZFLUX', data[:,5]), ('WFLUX', data[:,6]),
                     ('GFRAC', data[:,7]), ('RFRAC',data[:,8]), ('ZFRAC', data[:,9]), ('WFRAC', data[:,10])])
                   
    
    not_zero = np.where((data_dic['RFLUX']!=0) & (data_dic['ZFLUX']!=0) & (data_dic['WFLUX']!=0))
    not_zero = not_zero[0]

    r_cut = 10.0**((22.5-23.0)/2.5)    
    r_flux = data_dic['RFLUX'][not_zero]/data_dic['RFRAC'][not_zero]

    z_cut = 10.0**((22.5-20.56)/2.5)
    z_flux = data_dic['ZFLUX'][not_zero]/data_dic['ZFRAC'][not_zero]
    
    w1_cut = 10**((22.5-19.35)/2.5)
    w1_flux = data_dic['WFLUX'][not_zero]/data_dic['WFRAC'][not_zero]

    r_z_cut = 10**(1.6/2.5)
    
    lrg_true = np.where((r_flux > r_cut) & (z_flux > z_cut) & (w1_flux>w1_cut) &(z_flux > r_flux*r_z_cut)
                        &((w1_flux * (r_flux**(1.33-1.0))) > (z_flux**1.33 * 10**(-0.33/2.5))))

    print np.size(lrg_true)/(np.pi*radius**2)

    if con:
        con.close()
        
