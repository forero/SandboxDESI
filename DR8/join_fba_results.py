import fitsio
import numpy as np
import matplotlib.pyplot as plt
import json
from desitarget.targetmask import desi_mask, bgs_mask, mws_mask
import glob
from collections import Counter
from astropy.table import Table
import os

def join_fba_targets(program="bright", hemisphere="south"):
    summary_filename = "fba_summary_{}_{}.fits".format(program, hemisphere)
    if os.path.exists(summary_filename):
        print("Files {} {} already exist".format(summary_filename))
        return
    
    # read and sort targets
    targetdata = fitsio.read("targets/{}_{}.fits".format(program, hemisphere))
    targetdata = np.sort(targetdata, order='TARGETID')
    
    # list fba files
    fba_files = glob.glob("fba_{}_{}/fba-*.fits".format(program, hemisphere))
    print('{} fba_files to read'.format(len(fba_files)))
    # read fba files and list assigned and available targets
    t_assigned = []
    t_avail = []
    for fba_file in fba_files:
        fassign = fitsio.read(fba_file, ext="FASSIGN")
        favail = fitsio.read(fba_file, ext="FAVAIL")
        t_assigned.append(fassign["TARGETID"])
        t_avail.append(favail["TARGETID"])
    print('finished reading fba files')
    targetid_assigned = np.concatenate(t_assigned)
    targetid_available = np.concatenate(t_avail)
    
    # count the assigned targets
    counter_assigned = Counter(targetid_assigned)    
    print('finished counting targets')
    
    # find the ids and counts of the assigned targets
    id_assigned = np.array(list(counter_assigned.keys()))
    count_assigned = np.array(list(counter_assigned.values()))


    # sort the previous two lists by the target id
    ii = np.argsort(id_assigned)
    id_assigned = id_assigned[ii]
    count_assigned = count_assigned[ii]

    # trim the assigned targets to those in the input target data. this discards sky.
    is_target = np.isin(id_assigned, targetdata['TARGETID'])
    id_assigned = id_assigned[is_target]
    count_assigned = count_assigned[is_target]
    print('finished trimming targets')
    
    # new array of the same size as the input targets, will be filled with the 
    # number of times the target is assigned
    n_assigned = np.zeros(len(targetdata), dtype=int)
    ii = np.isin(targetdata['TARGETID'], id_assigned)
    n_assigned[ii] = count_assigned
    
    # new boolean array the same size as the input targets.
    # this tells me whether the target was available at all to the fibers.
    is_available = np.zeros(len(targetdata), dtype=bool)
    id_available = np.isin(targetdata['TARGETID'], targetid_available)
    is_available[id_available] = True
    
    # types of targets
    types = {'isELG':desi_mask['ELG'],
        'isLRG':desi_mask['LRG'],
        'isQSO':desi_mask['QSO'],
        'isBGS_ANY':desi_mask['BGS_ANY'],
        'isMWS_ANY':desi_mask['MWS_ANY']}
    
    print('assigning target types')
    # True or false depending on the type of target
    masks = {}
    for t, m in zip(types.keys(), types.values()):
        ii = (targetdata['DESI_TARGET']&m)!=0
        print(t, np.count_nonzero(ii))
        masks[t] = ii
        
    # convert to table and extend to write the final file to disk
    targettable = Table(targetdata)
    targettable['NUM_OBS']= n_assigned
    targettable['AVAIL'] = is_available
    for m in masks.keys():
        targettable[m] = masks[m]
        
    print('finished table')
    print('Writing to {}'.format(summary_filename))
    targettable.write(filename, overwrite=True)
    print('Done writing to {}'.format(summary_filename))

join_fba_targets(program="dark", hemisphere="south")
join_fba_targets(program="dark", hemisphere="north")
join_fba_targets(program="bright", hemisphere="south")
