# tiles designed for focal plane testing
import numpy as np
    
# environment setup https://desi.lbl.gov/trac/wiki/SurveyOps/DitherDesigns#Designingdithertiles
# source /global/project/projectdirs/desi/software/desi_environment.sh master
# module unload fiberassign/master
# module load fiberassign/5.3.0
# fba_cmx --dr=dr9 --dtver=0.49.0 --rundate=2021-11-25T21:00:00 --faflavor=dithprec --outdir=./ --tilera=0.0 --tiledec=84.9 --tileid=82412

coordinates = np.array([[0.0, 84.9],
                        [40.0, 84.0], 
                        [105.0, 84.0], 
                        [175,  83],
                        [215,  84.1],
                        [260,  84],
                        [322, 84.5],
                        [13.5, -20],
                        [31.6,  -20],
                        [48.5, -20],
                        [65, -18.9],
                        [84.3, -20],
                        [105.5, -18.4],
                        [123.8, -18.4],
                        [146, -20],
                        [167, -20],
                        [186,-20]]) 

options = ['dr=dr9', 'dtver=0.49.0', 'rundate=2021-11-25T21:00:00', 'seed=77', 
           'faflavor=dithprec', 'outdir=./']
           

ra = coordinates[:,0]
dec = coordinates[:,1]
#/global/cfs/cdirs/desi/survey/fiberassign/special/20210923/082/ 082268 already used
start_tileid = 82412
tileid = np.int_(start_tileid + 13*np.arange(len(ra)))
for i in range(len(ra)):
    ops = " --".join(options)
    comm = "fba_cmx --"+ ops 
    comm += " --tilera={}".format(ra[i])
    comm += " --tiledec={}".format(dec[i])
    comm += " --tileid={}".format(tileid[i])
    start_tileid = tileid[i]
    #print(comm)
    print("\t - Tiles {}-{}: dithprec at ra={}, dec={}".format(tileid[i], tileid[i]+12, ra[i], dec[i]))
    
#print("rm -Rf *{}*".format(start_tileid+1))
#print("rm -Rf *{}*".format(start_tileid+2))
#print("mv 082/* ./")
