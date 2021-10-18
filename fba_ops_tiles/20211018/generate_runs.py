# tiles designed for focal plane testing
import numpy as np
    

coordinates = np.array([[336.0 ,  30.0],
                        [1.40 ,  31.2], 
                        [31.0 ,  31.0], 
                        [52.50 ,  37.5],
                        [97.0, 36.5],
                        [105.5, 36.0],
                        [137.0, 36.0]])
options = ['dr=dr9', 'dtver=0.49.0', 'rundate=2021-10-18T21:00:00', 'seed=77', 
           'faflavor=dithprec', 'outdir=./']
           

ra = coordinates[:,0]
dec = coordinates[:,1]
#/global/cfs/cdirs/desi/survey/fiberassign/special/20210923/082/ 082268 already used
start_tileid = 82269
tileid = np.int_(start_tileid + 13*np.arange(len(ra)))
for i in range(len(ra)):
    ops = " --".join(options)
    comm = "fba_cmx --"+ ops 
    comm += " --tilera={}".format(ra[i])
    comm += " --tiledec={}".format(dec[i])
    comm += " --tileid={}".format(tileid[i])
    start_tileid = tileid[i]
    print(comm)
#    print("Tile {}: dithlost on ra={}, dec=+{}".format(tileid[i], ra[i], dec[i]))
    
#print("rm -Rf *{}*".format(start_tileid+1))
#print("rm -Rf *{}*".format(start_tileid+2))
#print("mv 082/* ./")
