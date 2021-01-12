import numpy as np
from astropy.table import Table

def print_run(flavor='science', tilera=0.0, tiledec=0.0, tileid=1, 
              scnd=False, priority='custom', fiber='restricted'):
 
    sv1_exec = 'python fba_scnd_sv1'
    if scnd:
        scnd_str = 'true'
    else:
        scnd_str = 'false'
        
    if fiber=='restricted':
        rundate = '2020-03-06T00:00:00'
    elif fiber=='unrestricted':
        rundate = '2020-01-01T00:00:00'
        
    run =  '{} --dr dr9 --dtver 0.47.0 --rundate {} '.format(sv1_exec, rundate)
    run += ' --tilera {} ' .format(tilera)
    run += ' --tiledec {} ' .format(tiledec)
    run += ' --tileid {} '.format(tileid)
    run += ' --faflavor {} '.format(flavor)
    run += ' --priority {}'.format(priority)
    if scnd:
        run += ' --scnd '
    run += ' --outdir ./tiles_sv1_scnd/{}_{}_scnd_{}_fiber_{}_{:06d} '.format(flavor, priority, scnd_str, fiber, tileid)
    return run

data = Table.read("sv1-tiles.fits")
flavors = ["sv1elg", "sv1elgqso","sv1lrgqso","sv1bgsmws"]

tileids = data['TILEID']+1000
ra = data['RA']
dec = data['DEC']
scnd = [True, False]
for i in range(len(tileids)):
    tileid = tileids[i]
    for flavor in flavors:
        for s in scnd:
            run = print_run(flavor=flavor, tilera=ra[i], tiledec=dec[i], tileid=tileid, scnd=s, priority='custom', fiber='restricted')
            print(run)

