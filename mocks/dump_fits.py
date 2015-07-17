import test_target as tt
import h5py
import sys
import numpy as np
from astropy.io import fits
import os

def get_tiles():
    """                                                                                                            
    input: none                                                                                                    
    output: numpy array with RA, DEC, PASS footprint information from desi-tiles.fits                              
    """
    tiling_file = os.path.join(os.environ['DESIMODEL'], 'data/footprint/', 'desi-tiles.fits')
    try:
        fin = fits.open(tiling_file)
        ww  = np.nonzero( fin[1].data['IN_DESI'])[0]
        ra_desi  = (fin[1].data['RA'][ww]).astype('f4')
        dec_desi  = (fin[1].data['DEC'][ww]).astype('f4')
        pass_desi = (fin[1].data['PASS'][ww]).astype('int')
        tileid_desi = (fin[1].data['TILEID'][ww]).astype('int')
    except Exception, e:
        import traceback
        print 'ERROR in get_tiles'
        traceback.print_exc()
        raise e
    return ra_desi, dec_desi, pass_desi, tileid_desi


single_fits = True

tile_ra = 190.0
tile_dec = 30.0
radius = 1.7
tile_id = 1
plate_radius_mm = 440

mockfile="/global/project/projectdirs/desi/mocks/lightcone_galform/Generic.r25-v0/Generic.r25/Gonzalez13.DB.MillGas.field1.photometry.0.hdf5"                                                                         

mockfile="/gpfs/data/Lightcone/lightcone_out/LC144/GAL437a/Generic.r25/Gonzalez13.DB.MillGas.field1.photometry.0.hdf5"
  
print mockfile
fin = h5py.File(mockfile, "r") 
data = fin.require_group('/Data') 
ra_data = data['ra'].value                                                                                    
dec_data = data['dec'].value                                                                                  
gal_id_string = data['GalaxyID'].value # these are string values, not integers!                               
g_decam = data['appDgo_tot_ext'].value                                                                        
r_decam = data['appDro_tot_ext'].value                                                                        
z_decam = data['appDzo_tot_ext'].value  

n_gals = 0
n_gals = ra_data.size
print n_gals, "ngals"
id_data = np.arange(n_gals)

if(single_fits):
    tt.select_targets(ra_data, dec_data, id_data, 
                      g_decam, r_decam, z_decam, 
                      tile_ra, tile_dec, tile_id)
else:
    print("let's tile")    
    ra_tiles, dec_tiles, pass_tiles, tileid = get_tiles() 
   
    id_mock = np.where((ra_tiles<ra_data.max())&(ra_tiles>ra_data.min())&(dec_tiles<dec_data.max())&(dec_tiles>dec_data.min()))
    id_mock = id_mock[0]
#print dec_tiles[id_decals], ra_tiles[id_decals], pass_tiles[id_decals], tileid[id_decals]                         
    n_tiles = np.size(id_mock)
    print dec_tiles[id_mock]

    for i in range(n_tiles):
        tile_ra = ra_tiles[id_mock[i]]
        tile_dec = dec_tiles[id_mock[i]]
        tile_id = tileid[id_mock[i]]
        
        x, y = tt.radec2xy(ra_data, dec_data, tile_ra, tile_dec)  

        distance = np.sqrt(x**2  + y**2)
        print "min max", distance.min(), distance.max()
        inside = np.where(distance < plate_radius_mm)
        inside = inside[0]
        
        n_in = np.size(inside)
        
        print "n in", n_in
        if(n_in>0):
            in_ra_data = ra_data[inside]
            in_dec_data = dec_data[inside]
            in_id_data = id_data[inside]
            in_g_decam = g_decam[inside]
            in_r_decam = r_decam[inside]
            in_z_decam = z_decam[inside]
            
            tt.select_targets(in_ra_data, in_dec_data, in_id_data,
                              in_g_decam, in_r_decam, in_z_decam,
                              tile_ra, tile_dec, tile_id)

