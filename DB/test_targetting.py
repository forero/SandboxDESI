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


    if con:
        con.close()
        
