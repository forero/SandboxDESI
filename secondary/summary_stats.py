from astropy.table import Table
from desitarget.sv1.sv1_targetmask import scnd_mask
import glob
import numpy as np
from collections import Counter, OrderedDict
import sys


#flavors ["sv1elg", "sv1elgqso","sv1lrgqso","sv1bgsmws"]
flavor = sys.argv[1]
priority = sys.argv[2]
print("flavor ", flavor)
print("priority", priority)

scnd = "true"
fba_files = glob.glob("tiles_sv1_scnd/{}_{}_scnd_{}_*/fiberassign-*.fits.gz".format(flavor, priority, scnd))
fba_files.sort()
print(len(fba_files))

scnd_targets = {}
names = [n for n in scnd_mask.names()]  

for n in names:
    scnd_targets[n] = {}
    scnd_targets[n]['n_avail'] = []
    scnd_targets[n]['n_assign'] = []
    
for i in range(len(fba_files)):
    flavor = fba_files[i].split('/')[1].split('_')[0]
    scnd = fba_files[i].split('/')[1].split('_')[3]
    targetid = fba_files[i].split('/')[1].split('_')[-1]
    data = Table.read(fba_files[i], hdu='FIBERASSIGN')
    pot = Table.read(fba_files[i], hdu='POTENTIAL_ASSIGNMENTS')
    targets = Table.read(fba_files[i], hdu='TARGETS')
    
    masks_assigned = data['SV1_SCND_TARGET'][data['SV1_SCND_TARGET']!=0]
    targetid_assigned = data['TARGETID'][data['SV1_SCND_TARGET']!=0]
    
    masks_targets = targets['SV1_SCND_TARGET'][targets['SV1_SCND_TARGET']!=0]
    targetid_targets = targets['TARGETID'][targets['SV1_SCND_TARGET']!=0]
    
    ii_pot = np.in1d(targetid_targets, pot['TARGETID'])
    masks_potential = masks_targets[ii_pot]
    targetid_potential = targetid_targets[ii_pot]
    #print(len(targetid_targets), len(targetid_potential), len(targetid_assigned))
    for n in names:
        ii_avail = (masks_potential & scnd_mask.mask(n))!=0
        ii_assigned = (masks_assigned & scnd_mask.mask(n))!=0
        n_avail = np.count_nonzero(ii_avail)
        n_assigned = np.count_nonzero(ii_assigned)
        scnd_targets[n]['n_avail'].append(n_avail)
        scnd_targets[n]['n_assign'].append(n_assigned)
        #print(n, n_avail, n_assigned)
    #print(flavor, targetid, n_scnd)

filename = 'scnd_summary_{}_{}.txt'.format(flavor, priority)
f = open(filename, 'w')
f.write('FAFLAVOR=`{}`, PRIORITY=`{}`\n'.format(flavor, priority))
f.write('||= SCND_MASK =||=N_AVAIL =||=N_ASSIGNED =||=Eff =||\n')
for n in names:
    if n!='VETO':
        f.write('|| {} || {} || {} || {:.4f} ||\n'.format(n, 
                                             np.sum(scnd_targets[n]['n_avail']), 
                                             np.sum(scnd_targets[n]['n_assign']),
                                            np.sum(scnd_targets[n]['n_assign'])/(1+np.sum(scnd_targets[n]['n_avail']))))

f.close()