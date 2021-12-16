import fitsio
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations, permutations


def compute_probability_distribution_1D(data):
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
        try:
            values.append(sorts[p])
        except:
            values.append(0.0)
    values = np.array(values)
    values = values/np.sum(values)

def compute_probability_distribution_2D(data, n_stride=2):
    s = np.shape(data)
    n_side = 2
    
    n_x = s[0]//n_stride -1
    n_y = s[1]//n_stride -1
    #print("computation over {} locations ".format(n_x*n_y))

    
    sorts = {}
    for i in range(n_x):
        for j in range(n_y):
            tmp = data[(i*n_stride) : (i*n_stride)+n_side, (j*n_stride):(j*n_stride)+n_side].flatten()
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
        try:
            values.append(sorts[p])
        except:
            values.append(0.0)
    values = np.array(values)
    values = values/np.sum(values)
    
    
    return values


def compute_entropy(proba_values):
    p = np.array(proba_values)
    entropy = np.sum(-p*np.log2(p))/np.log2(len(p))
    return entropy
