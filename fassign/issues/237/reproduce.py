"""
Simple file to reproduce issue #237 in fiberassign.


 The problem

 ICS uses Pandas dataframes to parse fiberassign tables, but Pandas doesn't support 2D columns. 
 When merging the target catalog into the FIBERASSIGN table, exclude 2D columns.
 Example problem at KPNO:

import fitsio
t = fitsio.read('/data/tiles/ALL_tiles/v1/fiberassign-059958.fits', 'FIBERASSIGN')
for name in t.dtype.names:
    if len(t[name].shape) > 1:
        print(name, t[name].shape)

...
DCHISQ (5000, 5)
"""

def create_simple_targets():

def create_simple_tiles():