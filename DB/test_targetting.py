import psycopg2
import sys
import numpy as np
from astropy.io import fits
import os


#arrays with target info
def extract_targets(ra, dec, radius, tile_id):
    n_qso = 0 
    n_elg = 0
    n_lrg = 0
    possible_types = ['ELG', 'LRG', 'QSO', 'STDSTAR', 'GAL', 'OTHER']

    priority = {'ELG': 4, 'LRG': 3, 'QSO': 1}
    nobs = {'ELG':1, 'LRG':2, 'QSO': 2}

    target_id = np.empty((0), dtype='int')
    target_db_id = np.empty((0), dtype='int')
    target_ra = np.empty((0))
    target_dec = np.empty((0))
    target_priority = np.empty((0), dtype='int')
    target_nobs = np.empty((0), dtype='int')
    target_types = np.empty((0))


    con = psycopg2.connect(host='scidb2.nersc.gov', user='desi_user', database='desi', password='decals_Fun!')
    cur = con.cursor()

    #LRG
    cur.execute("select candidate.id, candidate.ra, candidate.dec, decam.gflux, decam.rflux, decam.zflux, wise.w1flux, decam.g_ext, decam.r_ext, decam.z_ext, wise.w1_ext from  candidate, decam, wise where q3c_radial_query(candidate.ra, candidate.dec, %f, %f, %f) and decam.cand_id = candidate.id and wise.cand_id = candidate.id and decam.g_anymask =0  and decam.r_anymask =0 and decam.z_anymask=0;"%(ra,dec,radius))

    m=cur.fetchall()
    data = np.array(m)

    if(np.size(data)>0):

        data_dic = dict([('ID', data[:,0]), ('RA', data[:,1]), ('DEC', data[:,2]), 
                         ('GFLUX', data[:,3]), ('RFLUX', data[:,4]), ('ZFLUX', data[:,5]), ('WFLUX', data[:,6]),
                         ('GFRAC', data[:,7]), ('RFRAC',data[:,8]), ('ZFRAC', data[:,9]), ('WFRAC', data[:,10])])
        
        
        not_zero = np.where((data_dic['RFLUX']>0) & (data_dic['ZFLUX']>0) & 
                            (data_dic['WFLUX']>0) & (data_dic['GFLUX']>0))
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
        lrg_true = lrg_true[0]
        print "LRG", np.size(lrg_true)
        
        n_lrg = np.size(lrg_true)
        
        
        if(n_lrg>0):
    #update arrays to write
            target_db_id = np.append(target_db_id, np.int_(data_dic['ID'][not_zero[lrg_true]]))
            target_ra = np.append(target_ra, data_dic['RA'][not_zero[lrg_true]])
            target_dec = np.append(target_dec, data_dic['DEC'][not_zero[lrg_true]])
            target_priority = np.append(target_priority, np.int_(priority['LRG']*np.ones(n_lrg)))
            target_nobs = np.append(target_nobs, np.int_(nobs['LRG']*np.ones(n_lrg)))
            tmp_type = np.chararray(n_lrg, itemsize=8)
            tmp_type[:] = 'LRG'
            target_types = np.append(target_types, tmp_type)
            
            

    #ELG
    cur.execute("select candidate.id, candidate.ra, candidate.dec, decam.gflux, decam.rflux, decam.zflux, wise.w1flux, decam.g_ext, decam.r_ext, decam.z_ext, wise.w1_ext from  candidate, decam, wise where q3c_radial_query(candidate.ra, candidate.dec, %f, %f, %f) and decam.cand_id = candidate.id and wise.cand_id = candidate.id and decam.g_anymask =0  and decam.r_anymask =0 and decam.z_anymask=0;"%(ra,dec,radius))
    m=cur.fetchall()
    data = np.array(m)

    if(np.size(data)>0):
        data_dic = dict([('ID', data[:,0]), ('RA', data[:,1]), ('DEC', data[:,2]), 
                         ('GFLUX', data[:,3]), ('RFLUX', data[:,4]), ('ZFLUX', data[:,5]), ('WFLUX', data[:,6]),
                         ('GFRAC', data[:,7]), ('RFRAC',data[:,8]), ('ZFRAC', data[:,9]), ('WFRAC', data[:,10])])
            
        not_zero = np.where((data_dic['GFLUX']>0) & (data_dic['RFLUX']>0) & 
                            (data_dic['ZFLUX']>0) & (data_dic['WFLUX']>0))
        not_zero = not_zero[0]
            
        r_cut = 10.0**((22.5-23.4)/2.5)
        
        g_flux = data_dic['GFLUX'][not_zero]/data_dic['GFRAC'][not_zero]
        r_flux = data_dic['RFLUX'][not_zero]/data_dic['RFRAC'][not_zero]
        z_flux = data_dic['ZFLUX'][not_zero]/data_dic['ZFRAC'][not_zero]
        w1_flux = data_dic['WFLUX'][not_zero]/data_dic['WFRAC'][not_zero]
        
        

        elg_true = np.where((r_flux>r_cut) & (z_flux > (10**(0.3/2.5)*r_flux)) & (z_flux < (10**(1.5/2.5))*r_flux)&
                            (r_flux**2 < (g_flux * z_flux * 10**(-0.2/2.5))) & (z_flux < (g_flux * 10**(1.2/2.5))))
            
        elg_true = elg_true[0]
        n_elg = np.size(elg_true)
        print "ELG", np.size(elg_true)
        


#update arrays to write
        if(n_elg>0):
            target_db_id = np.append(target_db_id, np.int_(data_dic['ID'][not_zero[elg_true]]))
            target_ra = np.append(target_ra, data_dic['RA'][not_zero[elg_true]])
            target_dec = np.append(target_dec, data_dic['DEC'][not_zero[elg_true]])
            target_priority = np.append(target_priority, np.int_(priority['ELG']*np.ones(n_elg)))
            target_nobs = np.append(target_nobs, np.int_(nobs['ELG']*np.ones(n_elg)))
            tmp_type = np.chararray(n_elg, itemsize=8)
            tmp_type[:] = 'ELG'
            target_types = np.append(target_types, tmp_type)
            
    #QSO
    cur.execute("select candidate.id, candidate.ra, candidate.dec, decam.gflux, decam.rflux, decam.zflux, wise.w1flux, wise.w2flux, decam.g_ext, decam.r_ext, decam.z_ext, wise.w1_ext, wise.w2_ext from  candidate, decam, wise where q3c_radial_query(candidate.ra, candidate.dec, %f, %f, %f) and decam.cand_id = candidate.id and wise.cand_id = candidate.id and decam.g_anymask =0  and decam.r_anymask =0 and candidate.type='PSF' ;"%(ra,dec,radius))
    m=cur.fetchall()
    data = np.array(m)
    
    if(np.size(data)>0):
        data_dic = dict([('ID', data[:,0]), ('RA', data[:,1]), ('DEC', data[:,2]), 
                         ('GFLUX', data[:,3]), ('RFLUX', data[:,4]), ('ZFLUX', data[:,5]), ('W1FLUX', data[:,6]), ('W2FLUX', data[:,7]),
                         ('GFRAC', data[:,8]), ('RFRAC',data[:,9]), ('ZFRAC', data[:,10]), ('W1FRAC', data[:,11]),  ('W2FRAC', data[:,12])])
        
        not_zero = np.where((data_dic['GFLUX']>0) & (data_dic['RFLUX']>0) & (data_dic['ZFLUX']>0) 
                            & (data_dic['W1FLUX']>0) & (data_dic['W2FLUX']>0))
        
        not_zero = not_zero[0]
        
        r_cut = 10.0**((22.5-23.0)/2.5)

        g_flux = data_dic['GFLUX'][not_zero]/data_dic['GFRAC'][not_zero]
        r_flux = data_dic['RFLUX'][not_zero]/data_dic['RFRAC'][not_zero]
        z_flux = data_dic['ZFLUX'][not_zero]/data_dic['ZFRAC'][not_zero]
        w_flux = 0.75*data_dic['W1FLUX'][not_zero]/data_dic['W1FRAC'][not_zero] + 0.25*data_dic['W2FLUX'][not_zero]/data_dic['W2FRAC'][not_zero]
        
        qso_true = np.where((r_flux>r_cut)  & (r_flux < (g_flux * (10**(1.0/2.5)))) & 
                            (z_flux > 10**(-0.3/2.5)*r_flux)& (z_flux<10**(1.1/2.5)*r_flux) &((w_flux*(g_flux**1.2)) > (10**(-0.4/2.5) * (r_flux**(1.0+1.2)))))
        qso_true = qso_true[0]
        

        n_qso = np.size(qso_true)
        print "QSO", n_qso
    


#update arrays to write
        
        if(n_qso>0):
            target_db_id = np.append(target_db_id, np.int_(data_dic['ID'][not_zero[qso_true]]))
            target_ra = np.append(target_ra, data_dic['RA'][not_zero[qso_true]])
            target_dec = np.append(target_dec, data_dic['DEC'][not_zero[qso_true]])
            target_priority = np.append(target_priority, np.int_(priority['QSO']*np.ones(n_qso)))
            target_nobs = np.append(target_nobs, np.int_(nobs['QSO']*np.ones(n_qso)))
            tmp_type = np.chararray(n_qso, itemsize=8)
            tmp_type[:] = 'QSO'
            target_types = np.append(target_types, tmp_type)
            
    target_id = np.append(target_id, np.arange(np.size(target_ra), dtype='int'))
            
#write the samples in FITS format
    print (n_qso+n_lrg+n_elg   )
    if((n_qso+n_lrg+n_elg)>0):
       filename = "../data/Targets_Tile_%06d.fits"%(tile_id)
       
       c0=fits.Column(name='ID', format='K', array=target_id)
       c1=fits.Column(name='TARGETID', format='K', array=target_db_id)
       c2=fits.Column(name='RA', format='D', array=target_ra)
       c3=fits.Column(name='DEC', format='D', array=target_dec)
       c4=fits.Column(name='PRIORITY', format='D', array=target_priority)
       c5=fits.Column(name='NOBS', format='D', array=target_nobs)
       c6=fits.Column(name='OBJTYPE', format='8A', array=target_types)
       
       targetcat=fits.ColDefs([c0,c1,c2,c3,c4,c5,c6])

       table_targetcat_hdu=fits.TableHDU.from_columns(targetcat)
       table_targetcat_hdu.header['TILE_ID'] = tile_id       
       table_targetcat_hdu.header['TILE_RA'] = tile_id       
       table_targetcat_hdu.header['TILE_DEC'] = tile_id       
       

       hdu=fits.PrimaryHDU()
       hdulist=fits.HDUList([hdu])
       hdulist.append(table_targetcat_hdu)
       hdulist.verify()
       hdulist.writeto(filename)


    if con:
        con.close()
        
       
