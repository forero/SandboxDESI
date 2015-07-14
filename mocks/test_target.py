import h5py
import sys
import numpy as np
from astropy.io import fits
import os

def plate_dist(theta):
        """
        Returns the radial distance on the plate (mm) given the angle (radians).
        This is a fit to the provided data
        """
        p = np.array([8.297E5,-1750.0,1.394E4,0.0])
        radius = 0.0
        for i in range(4):
            radius = theta*radius + p[i]
        return radius

def radec2xy(object_ra, object_dec, tile_ra, tile_dec):
    """
    Returns the x,y coordinats of an object on the plate.
    It takes as an input the ra,dec coordinates ob the object 
    and the ra,dec coordinates of the plate's center.
    """
    object_theta = (90.0 - object_dec)*np.pi/180.0
    object_phi = object_ra*np.pi/180.0
    o_hat0 = np.sin(object_theta)*np.cos(object_phi)
    o_hat1 = np.sin(object_theta)*np.sin(object_phi)
    o_hat2 = np.cos(object_theta)
    
    tile_theta = (90.0 - tile_dec)*np.pi/180.0
    tile_phi = tile_ra*np.pi/180.0
    t_hat0 = np.sin(tile_theta)*np.cos(tile_phi)
    t_hat1 = np.sin(tile_theta)*np.sin(tile_phi)
    t_hat2 = np.cos(tile_theta)
    
    
    #we make a rotation on o_hat, so that t_hat ends up aligned with 
    #the unit vector along z. This is composed by a first rotation around z
    #of an angle pi/2 - phi and a second rotation around x by an angle theta, 
    #where theta and phi are the angles describin t_hat.
    
    costheta = t_hat2
    sintheta = np.sqrt(1.0-costheta*costheta) + 1E-10
    cosphi = t_hat0/sintheta
    sinphi = t_hat1/sintheta
    
    #First rotation, taking into account that cos(pi/2 -phi) = sin(phi) and sin(pi/2-phi)=cos(phi)
    n_hat0 = sinphi*o_hat0 - cosphi*o_hat1
    n_hat1 = cosphi*o_hat0 + sinphi*o_hat1
    n_hat2 = o_hat2
    
    #Second rotation
    nn_hat0 = n_hat0
    nn_hat1 = costheta*n_hat1 - sintheta*n_hat2
    nn_hat2 = sintheta*n_hat1 + costheta*n_hat2
    
    #Now find the radius on the plate
    theta = np.sqrt(nn_hat0*nn_hat0 + nn_hat1*nn_hat1)
    radius = plate_dist(theta)
    x = radius * nn_hat0/theta
    y = radius * nn_hat1/theta
    
    return x,y


def select_targets(ra_data, dec_data, gal_id, 
                   g_mags, r_mags, z_mags,
                   tile_ra, tile_dec, tile_id):


#    x, y = radec2xy(object_ra, object_dec, tile_ra, tile_dec)

#    mockfile="/global/project/projectdirs/desi/mocks/lightcone_galform/Generic.r25-v0/Generic.r25/Gonzalez13.DB.MillGas.field1.photometry.0.hdf5"
#    print mockfile
#    fin = h5py.File(mockfile, "r")
    
#    data = fin.require_group('/Data')


#    ra_data = data['ra'].value
#    dec_data = data['dec'].value
#    gal_id_string = data['GalaxyID'].value # these are string values, not integers!

#    g_decam = data['appDgo_tot_ext'].value
#    r_decam = data['appDro_tot_ext'].value
#    z_decam = data['appDzo_tot_ext'].value



#    n_gals = 0
#    n_gals = ra_data.size
#    print n_gals, "ngals"
#    gal_id = np.arange(n_gals)
        
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
    
    # LRG
#conditions on W1 magnitudes are missing from the LRG cuts
    lrg_true =  np.where((r_mags < 23.0) & (z_mags < 20.56) & ((r_mags-z_mags)>1.6))
    
    n_lrg = np.size(lrg_true) # goal is 350/deg^2
    print "LRG", n_lrg
        
    if(n_lrg>0):
    #update arrays to write                                                                                     
        target_db_id = np.append(target_db_id, np.int_(gal_id[lrg_true]))
        target_ra = np.append(target_ra, ra_data[lrg_true])
        target_dec = np.append(target_dec, dec_data[lrg_true])
        target_priority = np.append(target_priority, np.int_(priority['LRG']*np.ones(n_lrg)))
        target_nobs = np.append(target_nobs, np.int_(nobs['LRG']*np.ones(n_lrg)))
        tmp_type = np.chararray(n_lrg, itemsize=8)
        tmp_type[:] = 'LRG'
        target_types = np.append(target_types, tmp_type)
        
#ELG
        elg_true = np.where((r_mags < 23.4) & ((r_mags - z_mags)>0.3) & ((r_mags - z_mags)<1.5) & ((g_mags - r_mags)<(r_mags - z_mags - 0.2)) & ((g_mags - r_mags)< 1.2 - (r_mags - z_mags)))
        n_elg = np.size(elg_true) # goal is 2400/deg^2
        print "ELG", n_elg
        
    if(n_elg>0):
    #update arrays to write                                                                                     
        target_db_id = np.append(target_db_id, np.int_(gal_id[elg_true]))
        target_ra = np.append(target_ra, ra_data[elg_true])
        target_dec = np.append(target_dec, dec_data[elg_true])
        target_priority = np.append(target_priority, np.int_(priority['ELG']*np.ones(n_elg)))
        target_nobs = np.append(target_nobs, np.int_(nobs['ELG']*np.ones(n_elg)))
        tmp_type = np.chararray(n_elg, itemsize=8)
        tmp_type[:] = 'ELG'
        target_types = np.append(target_types, tmp_type)

        # QSO
        # goal is 260/deg^2
    print (n_qso+n_lrg+n_elg   )
    if((n_qso+n_lrg+n_elg)>0):
       filename = "../data/mock/Targets_Tile_%06d.fits"%(tile_id)

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
       table_targetcat_hdu.header['TILE_RA'] = tile_ra
       table_targetcat_hdu.header['TILE_DEC'] = tile_dec


    
       hdu=fits.PrimaryHDU()
       hdulist=fits.HDUList([hdu])
       hdulist.append(table_targetcat_hdu)
       hdulist.verify()
       hdulist.writeto(filename)


    
