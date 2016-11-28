import numpy as np


def init(n_small = 100 , n_large=10000):
    rand_large = np.random.randint(0, n_small, size=n_large)
    rand_small = np.arange(n_small, dtype='int')
    return rand_small, rand_large

def equal(rand_small, rand_large):
    a = rand_large.copy()
    for i in rand_small:
        ii = (rand_large == i)
        a[ii] = i
    return a

def wh(rand_small, rand_large):
    a = rand_large.copy()
    for i in rand_small:
        ii = np.where((rand_large == i))
        ii = ii[0]
        a[ii] = i
    return a

    

def dicc(rand_small, rand_large):
    a = rand_large.copy()
    d = {}
    
    s = list(set(rand_large))
    for i in s:
        d[i] = []

    for j in range(len(rand_large)):
        d[rand_large[j]].append(j)
        
    for i in rand_small:
        ii = d[i]
        a[ii] = i

    return a
