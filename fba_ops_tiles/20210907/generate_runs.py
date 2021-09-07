import numpy as np

# inside the footprint
coordinates = np.array([[278.00  , 36.5],
    [281.75  , 46.32],
    [336.00  , 30.0],
    [1.40 ,  31.2],
    [31.00 ,  31.0],
    [310.00 ,   0.0],
    [340.60  ,  0.0],
    [10.00  ,  0.0],
    [42.00  ,  0.0],
    [72.00 ,  -1.0]])


ra = coordinates[:,0]
dec = coordinates[:,1]
start_tileid = 85000
tileid = np.int_(start_tileid + np.arange(len(ra)))
options = ['doclean=n','dr=dr9','dtver=0.58.0','forcetileid=n',
           'gaiadr=gaiadr2' , 'goaltime=1000.0' , 'ha=0.0' , 
           'margin_gfa=0.0' , 'margin_petal=0.0' , 'margin_pos=0.0' , 'mintfrac=0.85', 'outdir=./' , 
           'pmcorr=n' , 'program=DARK', 'sky_per_petal=40' , 'sky_per_slitblock=1' ,'standards_per_petal=10' , 'survey=main']
           #'tiledec=20.0' , 'tileid=81100' , tilera=200.0
for i in range(len(ra)):
    ops = " --".join(options)
    comm = "fba_launch --"+ ops 
    comm += " --tilera={}".format(ra[i])
    comm += " --tiledec={}".format(dec[i])
    comm += " --tileid={}".format(tileid[i])
    start_tileid = tileid[i]
    print(comm)

    
# outside the footprint
coordinates = np.array([[320.00 ,  75.0],[4.50 ,  75.0], [40.00 ,  75.0], [66.50 ,  75.0]])
options = ['dr=dr9', 'dtver=0.49.0', 'rundate=2021-09-07T21:00:00', 'seed=77', 
           'faflavor=dithlost', 'outdir=./']
           

ra = coordinates[:,0]
dec = coordinates[:,1]
start_tileid = start_tileid+1
tileid = np.int_(start_tileid + np.arange(len(ra)))
for i in range(len(ra)):
    ops = " --".join(options)
    comm = "fba_cmx --"+ ops 
    comm += " --tilera={}".format(ra[i])
    comm += " --tiledec={}".format(dec[i])
    comm += " --tileid={}".format(tileid[i])
    start_tileid = tileid[i]
    print(comm)