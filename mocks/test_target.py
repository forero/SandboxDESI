
import h5py
import numpy as np

mockfile="/global/project/projectdirs/desi/mocks/lightcone_galform/Generic.r25-v0/Generic.r25/Gonzalez13.DB.MillGas.field1.photometry.0.hdf5"

fin = h5py.File(mockfile, "r")

data = fin.require_group('/Data')


ra = data['ra'].value
dec = data['dec'].value
gal_id_string = data['GalaxyID'].value # these are string values, not integers!

g_decam = data['appDgo_tot_ext'].value
r_decam = data['appDro_tot_ext'].value
z_decam = data['appDzo_tot_ext'].value

n_gals = ra.size

gal_id = np.arange(n_gals)

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

#conditions on W1 magnitudes are missing from the LRG cuts
lrg_true =  np.where((r_decam < 23.0) & (z_decam < 20.56) & ((r_decam-z_decam)>1.6))

n_lrg = np.size(lrg_true) # goal is 350/deg^2
print "LRG", n_lrg/50.0


elg_true = np.where((r_decam < 23.4) & ((r_decam - z_decam)>0.3) & ((r_decam - z_decam)<1.5) & ((g_decam - r_decam)<(r_decam - z_decam - 0.2)) & ((g_decam - r_decam)< 1.2 - (r_decam - z_decam)))
n_elg = np.size(elg_true) # goal is 2400/deg^2
print "ELG", n_elg/50.0



#qso is 260/deg^2
