import fitsio
import os
import desitarget.io as dtio
from astropy.table import Table

root = '/global/project/projectdirs/desi/users/forero/datachallenge2017/test_201703/test/'
iter_truth = dtio.iter_files(root, 'truth')
iter_target = dtio.iter_files(root, 'targets')

n = 0
for truth_file, target_file in zip(iter_truth, iter_target):
    truth = Table.read(truth_file)
    targets = Table.read(target_file)
    print(truth_file, target_file)

#path = '/global/project/projectdirs/desi/users/forero/datachallenge2017/test_201703/test/209'
#truth_filename = os.path.join(path, 'truth-2090m020.fits')
#file = fitsio.FITS(truth_filename)
#wave = file['WAVE'].read()
#flux = file['FLUX'].read()
#truth = file['FLUX'].read()
