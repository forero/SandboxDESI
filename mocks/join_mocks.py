
# coding: utf-8

# In[19]:

import h5py 
import numpy as np
import os
import glob
from astropy.table import Table
import desimodel.footprint


# In[2]:

names = {'sources1':'LRG', 'sources2':'ELG', 'sources3':'QSO'}
datafields = ['RA', 'DEC', 'Z_COSMO', 'DZ_RSD']
summary = {}
for name in names.keys():
    summary[names[name]] = {}
    for field in datafields:
        summary[names[name]][field] = np.empty((0))


# In[3]:

datapath = '/global/project/projectdirs/desi/mocks/GaussianRandomField/v0.0.6_2LPT'
datafiles = glob.glob(datapath+"/*.h5")


# In[4]:

for datafile in datafiles:
    f = h5py.File(datafile, "r")
    for source in names.keys():
        s = f[source]
        for field in datafields:
            data = s[field]
            print(source, field, len(data), type(data))
            if len(data)>0 :
                summary[names[source]][field] = np.append(summary[names[source]][field], data)


# In[6]:

desitiles = desimodel.io.load_tiles()
for source in names.values():
    indesi = desimodel.footprint.is_point_in_desi(desitiles, summary[source]['RA'], summary[source]['DEC'])
    for field in datafields:
        data = summary[source][field] 
        summary[source][field] = data[indesi]


# In[20]:

for source in names.values():
    Table(summary[source]).write(source+'.fits', overwrite=True)


# In[ ]:



