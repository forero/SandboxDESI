import psycopg2
import sys
import numpy as np

con = psycopg2.connect(host='scidb2.nersc.gov', user='desi_user', database='desi')
cur = con.cursor()

cur.execute("select id, ra, dec from candidate where q3c_radial_query(candidate.ra, candidate.dec, 240.0, 7.0,0.01);")

m=cur.fetchall()

print len(m)
print m[1]


m_array  = np.array(m)
print np.shape(m_array)
for line in m_array:
    print line

if con:
    con.close()
