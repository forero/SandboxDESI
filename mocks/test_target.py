
import h5py

mockfile="/global/project/projectdirs/desi/mocks/lightcone_galform/Generic.r25-v0/Generic.r25/Gonzalez13.DB.MillGas.field1.photometry.0.hdf5"

fin = h5py.File(mockfile, "r")

data = fin.require_group('/Data')


ra = data['ra'].value
dec = data['dec'].value
gal_id_string = data['GalaxyID'].value # these are string values, not integers!

g_decam = data['appDgo_tot_ext'].value
r_decam = data['appDro_tot_ext'].value
z_decam = data['appDzo_tot_ext'].value
