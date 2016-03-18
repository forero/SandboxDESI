import numpy as np
import desitarget.mtl
import os
import shutil
from desisim.quickcat import quickcat
import glob
import subprocess
from astropy.table import Table, Column
import os.path

def mtl_assign_quickcat_loop(output_path=None, targets_path=None, zcat_file=None, fiberassign_exec=None, epoch_path=None, 
                             epoch_id=0, fiber_epochs=[], mtl_epochs=[], perfect=True):

    # create temporary output paths
    tmp_output_path = os.path.join(output_path, 'tmp/')
    if not os.path.exists(tmp_output_path):
        os.makedirs(tmp_output_path)

    tmp_fiber_path = os.path.join(tmp_output_path, 'fiberassign/')
    if not os.path.exists(tmp_fiber_path):
        os.makedirs(tmp_fiber_path)

    # create survey list from mtl_epochs IDS
    surveyfile = os.path.join(tmp_output_path, "survey_list.txt")
    ids = []
    for i in mtl_epochs:
        epochfile = os.path.join(epoch_path, "epoch{}.txt".format(i))        
        ids = np.append(ids, np.loadtxt(epochfile))

    ids = np.int_(ids)
    np.savetxt(surveyfile, ids, fmt='%d')
    print("{} tiles to be included in fiberassign".format(len(ids)))

    #load truth / targets / zcat
    truth = Table.read(os.path.join(targets_path,'truth.fits'))
    targets = Table.read(os.path.join(targets_path,'targets.fits'))
    
    if zcat_file is None:
        mtl = desitarget.mtl.make_mtl(targets)
        mtl.write(os.path.join(tmp_output_path, 'mtl.fits'), overwrite=True)
    else:
        zcat = Table.read(zcat_file, format='fits')
        mtl = desitarget.mtl.make_mtl(targets, zcat)
        mtl.write(os.path.join(tmp_output_path, 'mtl.fits'), overwrite=True)
    print("Finished MTL")

    # clean all fibermap fits files before running fiberassing
    tilefiles = sorted(glob.glob(tmp_fiber_path+'/tile*.fits'))
    if tilefiles:
        for tilefile in tilefiles:
            os.remove(tilefile)
            
    # launch fiberassign
    print("Launched fiberassign")
    p = subprocess.call([fiberassign_exec, os.path.join(tmp_output_path, 'fa_features.txt')], stdout=subprocess.PIPE)
    #p = subprocess.call([fiberassign_exec, os.path.join(tmp_output_path, 'fa_features.txt')])
    print("Finished fiberassign")


    #create a list of fibermap tiles to read and update zcat
    ids = []
    for i in fiber_epochs:
        epochfile = os.path.join(epoch_path, "epoch{}.txt".format(i))        
        ids = np.append(ids, np.loadtxt(epochfile))
    ids = np.int_(ids)


    tilefiles = []
    for i in ids:
        tilename = os.path.join(tmp_fiber_path, 'tile_%05d.fits'%(i))
        if os.path.isfile(tilename):
            tilefiles.append(tilename)
        else:
            print('Suggested but does not exist {}'.format(tilename))
    print("{} tiles to gather in fiberassign output".format(len(tilefiles)))
    
    # write the zcat
    if zcat_file is None:
        zcat_file = os.path.join(tmp_output_path, 'zcat.fits')
        zcat = quickcat(tilefiles, targets, truth, zcat=None, perfect=perfect)
        zcat.write(zcat_file, overwrite=True)
    else:
        zcat_file = os.path.join(tmp_output_path, 'zcat.fits')
        zcat = Table.read(zcat_file, format='fits')
        newzcat = quickcat(tilefiles, targets, truth, zcat=zcat, perfect=perfect)
        newzcat.write(zcat_file, format='fits', overwrite=True)
    print("Finished zcat")

    # keep a copy of zcat.fits per epoch
    epoch_output_path = os.path.join(output_path, '{}'.format(epoch_id))
    if not os.path.exists(epoch_output_path):
        os.makedirs(epoch_output_path)        
    shutil.copy(zcat_file, epoch_output_path)

    # keep a copy of mtl.fits per epoch
    shutil.copy(os.path.join(tmp_output_path, 'mtl.fits'), epoch_output_path)

    # keep a copy of all the fiberassign files per epoch
    fiber_epoch_output_path = os.path.join(epoch_output_path, 'fiberassign')
    if not os.path.exists(fiber_epoch_output_path):
        os.makedirs(fiber_epoch_output_path)
    tilefiles = sorted(glob.glob(tmp_fiber_path+'/tile*.fits'))
    if tilefiles:
        for tilefile in tilefiles:
            shutil.copy(tilefile, fiber_epoch_output_path)

    return zcat_file



epoch_path = "/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/"
targets_path = "/project/projectdirs/desi/mocks/preliminary/mtl/lowfat/"
fiberassign_exec = "/global/homes/f/forero/fiberassign/bin/./fiberassign"



# new kind of setup
output_path =  "/project/projectdirs/desi/users/forero/lowfat/"
if not os.path.exists(output_path):
    os.makedirs(output_path)

tmp_output_path = os.path.join(output_path, 'tmp/')
if not os.path.exists(tmp_output_path):
    os.makedirs(tmp_output_path)

tmp_fiber_path = os.path.join(tmp_output_path, 'fiberassign/')
if not os.path.exists(tmp_fiber_path):
    os.makedirs(tmp_fiber_path)

# create temporaty input file for fiberassign
params = ''.join(open('template_fiberassign.txt').readlines())
fx = open(os.path.join(tmp_output_path, 'fa_features.txt'), 'w')
fx.write(params.format(inputdir=tmp_output_path, targetdir=targets_path))
fx.close()

# loop over the epochs
n_epochs = 5
zcat_file = None
for i in range(n_epochs):
    zcat_file = mtl_assign_quickcat_loop( 
        output_path = output_path, targets_path = targets_path,
        zcat_file = zcat_file, fiberassign_exec = fiberassign_exec, epoch_path = epoch_path,
        epoch_id = i, 
        fiber_epochs = [i], mtl_epochs = range(i,n_epochs), perfect=False)

# run everything on a single epoch
zcat_file = None
zcat_file = mtl_assign_quickcat_loop( 
    output_path = output_path, targets_path = targets_path,
    zcat_file = zcat_file, fiberassign_exec = fiberassign_exec, epoch_path = epoch_path,
    epoch_id = n_epochs, 
    fiber_epochs = range(n_epochs), mtl_epochs = range(n_epochs), perfect=False)

#clean up tmp directory
if os.path.exists(tmp_output_path):
    shutil.rmtree(tmp_output_path)
