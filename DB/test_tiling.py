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

#get the tiles in desi
ra_tiles, dec_tiles, pass_tiles = get_tiles()

#open database connection
con = psycopg2.connect(host='scidb2.nersc.gov', user='desi_user', database='desi')
cur = con.cursor()

#file to write the data
out = open("../data/decals_ngals.dat", "w")
out.write("# number of decals sources in a circle of 0.7 deg in radius")
out.write("# index, ra , dec , ipass , ngaln")

#loop over tiles to count the number of galaxies inside
index = 0
for ra, dec, ipass in zip(ra_tiles, dec_tiles, pass_tiles):
    cur.execute("select id, ra, dec from candidate where q3c_radial_query(candidate.ra, candidate.dec, %f, %f,0.7);"%(ra,dec))
    m=cur.fetchall()
    index = index+1
    if(len(m)):
        out.write("%d %f %f %d %d\n"%(index, ra, dec, ipass, len(m)))

if con:
    con.close()
