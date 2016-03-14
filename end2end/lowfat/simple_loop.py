import numpy as np
from fiberassign.mock import rdzipn2targets
from desitarget.targets import desi_mask
import desitarget.mtl

def assign_quickcat_mtl_loop(destination_path=None, mtl_path = None, zcat_path =  None,
                             targets_file=None, truth_file=None, zcat_file=None,
                             fiberassign_exec=None, fiberassign_features=None, fiberassign_output_path=None, 
                             quickcat_source_file = None):
    from astropy.table import Table, Column
    truth = Table.read(truth_file)
    targets = Table.read(targets_file)
    
    if zcat_file is None:
        mtl = desitarget.mtl.make_mtl(targets)
        mtl.write('mtl.fits', overwrite=True)
    else:
        zcat = Table.read(zcat_file, format='fits')
        mtl = desitarget.mtl.make_mtl(targets, zcat)
        mtl.write('mtl.fits', overwrite=True)

    import glob
    import shutil
    shutil.copy('mtl.fits', mtl_path)

    # I had to go first into fiberassign to run make && make install 
    import subprocess
    import os
    p = subprocess.call([fiberassign_exec, fiberassign_features], stdout=subprocess.PIPE)

    #find the tiles
    from glob import glob
    tilefiles = sorted(glob(fiberassign_output_path+'/tile*.fits'))
    print("{} tiles in fiberassign output".format(len(tilefiles)))

    import imp
    # this ugly hack avoids import from desi stack
    desisim = imp.load_source("desisim.quickcat", quickcat_source_file)
    # import os
    # os.chdir('/global/homes/f/forero/desisim/py')

    #from desisim.quickcat import quickcat
    if zcat_file is None:
        zcat = desisim.quickcat(tilefiles, targets, truth, zcat=None, perfect=False)
        zcat.write('zcat.fits', overwrite=True)
    else:
        zcat = Table.read(zcat_file, format='fits')
        newzcat = desisim.quickcat(tilefiles, targets, truth, zcat=zcat, perfect=False)
        newzcat.write('zcat.fits', format='fits', overwrite=True)

    shutil.copy('zcat.fits', zcat_path)
    shutil.copy('zcat.fits', destination_path)

    #clean files
    import os
    for tilefile in tilefiles:
        os.remove(tilefile)


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

epoch_path = "/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/"
base_output_path = "/project/projectdirs/desi/users/forero/epochs/"
targets_path = "/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/"
mtl_path = "/project/projectdirs/desi/users/forero/mtl/"
zcat_path = "/project/projectdirs/desi/users/forero/zcat/"
desitiles_path =  "/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/"
desitiles_file = "lowfat-desi-tiles.par"
fiberassign_exec = "/global/homes/f/forero/fiberassign/bin/./fiberassign"
fiberassign_features = "/global/homes/f/forero/SandboxDESI/end2end/lowfat/fa_features.txt"
fiberassign_output_path = "/project/projectdirs/desi/users/forero/fiberassign"
quickcat_source_file  = "/global/homes/f/forero/desisim/py/desisim/quickcat.py"
n_epochs = 5

for i in range(n_epochs):

    epochfile = os.path.join(epoch_path, "epoch{}.txt".format(i))
    tmp_output_path = os.path.join(base_output_path, "{}".format(i))
    print(tmp_output_path)
    print(epochfile)
    if not os.path.exists(tmp_output_path):
        os.makedirs(tmp_output_path)
    
    desitiles = os.path.join(desitiles_path, desitiles_file)
    write_epoch_file(desitiles=desitiles, epochfile=epochfile)
    
    if i==0:
        assign_quickcat_mtl_loop(destination_path = tmp_output_path, mtl_path = mtl_path, zcat_path = zcat_path,
                                 targets_file = os.path.join(targets_path, "targets.fits"), 
                                 truth_file = os.path.join(targets_path,"truth.fits"), 
                                 fiberassign_exec = fiberassign_exec, 
                                 fiberassign_features = fiberassign_features,
                                 fiberassign_output_path = fiberassign_output_path,
                                 quickcat_source_file = quickcat_source_file)
    else:        
        assign_quickcat_mtl_loop(destination_path = tmp_output_path, mtl_path = mtl_path, zcat_path = zcat_path,
                                 targets_file = os.path.join(targets_path, "targets.fits"), 
                                 truth_file = os.path.join(targets_path,"truth.fits"), 
                                 zcat_file = os.path.join(zcat_path, "zcat.fits"),
                                 fiberassign_exec = fiberassign_exec, 
                                 fiberassign_features = fiberassign_features,
                                 fiberassign_output_path = fiberassign_output_path,
                                 quickcat_source_file = quickcat_source_file)

