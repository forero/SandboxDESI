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
out.write("# number of decals sources in a circle of 0.7 deg in radius\n")
out.write("# index, ra , dec , ipass , ngaln\n")
out.close()

#loop over tiles to count the number of galaxies inside
index = 0
n_tiles = np.size(pass_tiles)
for i in range(10):
    cur.execute("select id, ra, dec from candidate where q3c_radial_query(candidate.ra, candidate.dec, %f, %f,0.7);"%(ra_tiles[i],dec_tiles[i]))
    m=cur.fetchall()
    print "looking for in", i
    if(len(m)):
        out = open("../data/decals_ngals.dat", "a")
        print "something in", i
        out.write("%d %f %f %d %d\n"%(i, ra_tiles[i], dec_tiles[i], pass_tiles[i], len(m)))
        out.close()
if con:
    con.close()
