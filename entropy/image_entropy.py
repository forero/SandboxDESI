import fitsio
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations, permutations

def compute_probability_distribution(data):
    s = np.shape(data)
    n_side = 2
    n_x = s[0]-1
    n_y = s[1]-1

    
    sorts = {}
    for i in range(0,n_x):
        for j in range(0,n_y):
            tmp = data[i : i+n_side, j:j+n_side].flatten()
            sorted_ids = np.int_(np.argsort(tmp))
            s = ''.join(str(j) for j in sorted_ids)
            try:
                sorts[s] += 1
            except:
                sorts[s] = 1
    
    # return the probabilities in the order provided by the permutations routine
    a = '0123'
    perms = permutations(a, 4)
    sorted_perms = []
    for p in perms:
        sorted_perms.append(''.join(i for i in p))
        
    values = []
    for p in sorted_perms:
        values.append(sorts[p])
    values = np.array(values)
    values = values/np.sum(values)
    
    
    return values


def compute_entropy(proba_values):
    p = np.array(proba_values)
    entropy = np.sum(-p*np.log2(p))/np.log2(len(p))
    return entropy

def read_sky_sframe(sframe_file):
    h = fitsio.FITS(sframe_file)
    sel = h["FIBERMAP"]["OBJTYPE"].read() == "SKY"
    sky = h["FLUX"].read()[sel,:]
    return sky

def compute_camera_entropy(exp_path, date, expid, band):
    n_petals = 10
    skyb_petals = []
    for i in range(n_petals):
        filename = '{}/{}/{:08d}/sframe-{}{}-{:08d}.fits'.format(exp_path, date, expid, band, i, expid)
        skyb_petals.append(read_sky_sframe(filename))
        #print('read ', i)
    
    p_skyb_petals = []
    for i in range(n_petals):
        p_skyb_petals.append(compute_probability_distribution(skyb_petals[i]))
        #print('probability', i)

    entropy_p_skyb_petals = []
    for i in range(n_petals):
        entropy_p_skyb_petals.append(compute_entropy(p_skyb_petals[i]))
        #print('entropy', i)
    return np.array(entropy_p_skyb_petals)