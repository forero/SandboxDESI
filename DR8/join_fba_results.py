import fitsio
import numpy as np
import matplotlib.pyplot as plt
import json
from desitarget.targetmask import desi_mask, bgs_mask, mws_mask
import glob
from collections import Counter
from astropy.table import Table
import os

def join_fba_targets(path_to_data="./", program="bright", hemisphere="south"):
    
    print("program {} hemisphere {}".format(program, hemisphere))
    summary_filename = "{}/fba_summary_{}_{}.fits".format(path_to_data, program, hemisphere)
    if os.path.exists(summary_filename):
        print("File  {} already exists".format(summary_filename))
        return
    
    # read and sort targets
    targetdata = fitsio.read("{}/targets/{}_{}.fits".format(path_to_data, program, hemisphere))
    targetdata = np.sort(targetdata, order='TARGETID')
    
    # list fba files
    fba_files = glob.glob("{}/fba_{}_{}/fba-*.fits".format(path_to_data, program, hemisphere))
    print('{} fba_files to read'.format(len(fba_files)))
    # read fba files and list assigned and available targets
    t_assigned = []
    t_avail_fiber = []
    t_avail_tile = []
    for fba_file in fba_files:
        fassign = fitsio.read(fba_file, ext="FASSIGN")
        favail = fitsio.read(fba_file, ext="FAVAIL")
        t_assigned.append(fassign["TARGETID"])
        t_avail_fiber.append(favail["TARGETID"])
        t_avail_tile.append(list(set(favail["TARGETID"])))
    print('finished reading fba files')
    targetid_assigned = np.concatenate(t_assigned)
    targetid_available_fiber = np.concatenate(t_avail_fiber)
    targetid_available_tile = np.concatenate(t_avail_tile)
    
    # count the assigned targets
    counter_assigned = Counter(targetid_assigned)    
    print('finished counting targets')
    
    # count the available targets per fiber
    counter_available_fiber = Counter(targetid_available_fiber)
    print('finished counting available per fiber')
    
    # count the available targets per fiber
    counter_available_tile = Counter(targetid_available_tile)
    print('finished counting available per tile')
    
    # find the ids and counts of the assigned targets
    id_assigned = np.array(list(counter_assigned.keys()))
    count_assigned = np.array(list(counter_assigned.values()))

    # find the ids and counts of the available targets per fiber
    id_available_fiber = np.array(list(counter_available_fiber.keys()))
    count_available_fiber = np.array(list(counter_available_fiber.values()))
    
    # find the ids and counts of the available targets per tile
    id_available_tile = np.array(list(counter_available_tile.keys()))
    count_available_tile = np.array(list(counter_available_tile.values()))
    
    # sort the previous three lists by the target id
    ii = np.argsort(id_assigned)
    id_assigned = id_assigned[ii]
    count_assigned = count_assigned[ii]

    ii = np.argsort(id_available_fiber)
    id_available_fiber = id_available_fiber[ii]
    count_available_fiber = count_available_fiber[ii]

    ii = np.argsort(id_available_tile)
    id_available_tile = id_available_tile[ii]
    count_available_tile = count_available_tile[ii]
    
    # trim the targets in these lits to those in the input target data. this discards sky.
    is_target = np.isin(id_assigned, targetdata['TARGETID'])
    id_assigned = id_assigned[is_target]
    count_assigned = count_assigned[is_target]

    is_target = np.isin(id_available_fiber, targetdata['TARGETID'])
    id_available_fiber = id_available_fiber[is_target]
    count_available_fiber = count_available_fiber[is_target]

    is_target = np.isin(id_available_tile, targetdata['TARGETID'])
    id_available_tile = id_available_tile[is_target]
    count_available_tile = count_available_tile[is_target]
    
    # new array of the same size as the input targets, will be filled with the 
    # number of times the target is assigned
    n_assigned = np.zeros(len(targetdata), dtype=int)
    ii = np.isin(targetdata['TARGETID'], id_assigned)
    n_assigned[ii] = count_assigned
    
    # new array of the same size as the input targets, will be filled with the 
    # number of times the target is available to a fiber
    n_available_fiber = np.zeros(len(targetdata), dtype=int)
    ii = np.isin(targetdata['TARGETID'], id_available_fiber)
    n_available_fiber[ii] = count_available_fiber
    
    
    # new array of the same size as the input targets, will be filled with the 
    # number of times the target is available to a tile
    n_available_tile = np.zeros(len(targetdata), dtype=int)
    ii = np.isin(targetdata['TARGETID'], id_available_tile)
    n_available_tile[ii] = count_available_tile
    
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
    targettable['NUMOBS']= n_assigned
    targettable['NAVAIL_FIBER'] = n_available_fiber
    targettable['NAVAIL_TILE'] = n_available_tile

    for m in masks.keys():
        targettable[m] = masks[m]
        
    print('finished table')
 
    print('Writing to {}'.format(summary_filename))
    targettable.write(summary_filename, overwrite=True)
    print('Done writing to {}'.format(summary_filename))

join_fba_targets(path_to_data="0.38.0", program="dark", hemisphere="north")
join_fba_targets(path_to_data="0.38.0", program="bright", hemisphere="north")
join_fba_targets(path_to_data="0.38.0", program="dark", hemisphere="south")
join_fba_targets(path_to_data="0.38.0", program="bright", hemisphere="south")
