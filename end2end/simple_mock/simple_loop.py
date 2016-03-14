# testing different PRs
# @home on the login node at Edison
# executed line by line on IPython

import numpy as np
from fiberassign.mock import rdzipn2targets
from desitarget.targets import desi_mask
import desitarget.mtl

# first iteration to create the targets and truth.
def make_targets():
    targets, truth = rdzipn2targets('/project/projectdirs/desi/mocks/preliminary/objects_ss_sf0.rdzipn')

    print 'targets.colnames = ', targets.colnames
    print 'truth.colnames = ', truth.colnames

    iisky = (targets['DESI_TARGET'] & desi_mask.SKY) != 0
    iistd = (targets['DESI_TARGET'] & desi_mask.STD_FSTAR) != 0
    iiobj = (~iisky & ~iistd)
    print np.count_nonzero(iisky), np.count_nonzero(iistd), np.count_nonzero(iiobj)
    
    targets[iiobj].write('targets.fits', overwrite=True)
    targets[iisky].write('sky.fits', overwrite=True)
    targets[iistd].write('stdstars.fits', overwrite=True)
    truth[iiobj].write('truth.fits', overwrite=True)




def assign_quickcat_mtl_loop(destination_dir="./", targets_file="", truth_file=""):
    from astropy.table import Table, Column
    truth = Table.read(truth_file)
    targets = Table.read(targets_file)
    # this part tests another PR https://github.com/desihub/desitarget/pull/32
    mtl = desitarget.mtl.make_mtl(targets)
    mtl.write('mtl.fits', overwrite=True)

    import glob
    import shutil
    for f in glob.glob("*.fits"): 
        shutil.copy(f, "/project/projectdirs/desi/users/forero/mtl")

    # this now tests another PR https://github.com/desihub/fiberassign/pull/24
    # I had to go first into fiberassign to run make && make install 
    import subprocess
    p = subprocess.call(["./fiberassign/bin/./fiberassign", "fa_features.txt"], stdout=subprocess.PIPE)

    #find the tiles
    from glob import glob
    tiledir = '/project/projectdirs/desi/users/forero/fiberassign'
    tilefiles = sorted(glob(tiledir+'/tile*.fits'))
    len(tilefiles)

    import imp
    # this ugly hack avoids import from desi stack
    desisim = imp.load_source("desisim.quickcat", "/global/homes/f/forero/desisim/py/desisim/quickcat.py")
    # import os
    # os.chdir('/global/homes/f/forero/desisim/py')

    #from desisim.quickcat import quickcat
    zcat = desisim.quickcat(tilefiles, targets, truth, zcat=None, perfect=False)
    zcat.write('zcat.fits', overwrite=True)

def write_epoch_file(desitiles="desi-tiles.par", epochfile="dark_epoch0.txt", epochtiles="epoch-desi-tiles.par"):
    filein = open(desitiles, "r")
    tilelines = filein.readlines()
    filein.close()
    tiles = np.loadtxt(epochfile)

    fileout = open(epochtiles, "w")
    for line in tilelines:
        words = line.split()
        if(len(words) < 5):
            fileout.write("{}".format(line))
        else:
            tile = int(words[1])
            in_desi = int(words[4])
            if in_desi == 0:
                raise NameError('TileNotInDESI')
            if tile in tiles:
                fileout.write("{}".format(line))
    fileout.close()

import os
epochdir = "/project/projectdirs/desi/datachallenge/Argonne2015/opsim2.1/epochs/"
base_output_dir = "/project/projectdirs/desi/users/forero/epochs/"
n_epochs = 1
for i in range(n_epochs):

    epochfile = os.path.join(epochdir, "dark_epoch{}.txt".format(i))
    tmp_output_dir = os.path.join(base_output_dir, "{}".format(i))
    print(tmp_output_dir)
    print(epochfile)
    if not os.path.exists(tmp_output_dir):
        os.makedirs(tmp_output_dir)
    
    desitiles = "/project/projectdirs/desi/software/edison/desimodel/0.3.1/data/footprint/desi-tiles.par"
    write_epoch_file(desitiles=desitiles, epochfile=epochfile)
    
    assign_quickcat_mtl_loop()
