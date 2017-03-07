import fitsio
import os
import desitarget.io as dtio
from astropy.table import Table, vstack

root = '/global/project/projectdirs/desi/users/forero/datachallenge2017/test_201703/test/'
iter_truth = dtio.iter_files(root, 'truth')
iter_target = dtio.iter_files(root, 'targets')

alltruth = []
alltargets = []
for truth_file, target_file in zip(iter_truth, iter_target):
    alltruth.append(Table.read(truth_file))
    alltargets.append(Table.read(target_file))
    print(truth_file, target_file)


targets = vstack(alltargets)
truth = vstack(alltruth)

out_targets = os.path.join(root,'targets.fits')
out_truth = os.path.join(root,'truth.fits')
targets.write(out_targets)
truth.write(out_truth)

print(truth)
print(targets)
