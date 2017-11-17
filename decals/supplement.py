from astropy.table import Table
import astropy
import desitarget.mock.build as mb
import numpy as np
from desitarget.targetmask import desi_mask, bgs_mask, mws_mask
import desitarget.mtl

targetsfilename = "targets-dr5.0-0.16.2.fits"
targetsfilename = "small_chunk_targets-dr5.0-0.16.2.fits"
targets = Table.read(targetsfilename)
nobj = len(targets)
truth = mb.empty_truth_table(nobj=nobj)
for k in targets.keys():
    if k in truth.keys():
        print(k)
        truth[k][:] = targets[k][:]

nothing = '          '
truth['TEMPLATESUBTYPE'] = np.repeat(nothing, nobj)


masks = ['BGS_ANY', 'ELG', 'LRG', 'QSO', 'STD_FSTAR', 'STD_BRIGHT']
dict_truspectype = {'BGS_ANY':'GALAXY', 'ELG':'GALAXY', 'LRG':'GALAXY', 'QSO':'QSO', 
                    'STD_FSTAR':'STAR', 'STD_BRIGHT':'STAR'}
dict_truetemplatetype = {'BGS_ANY':'BGS', 'ELG':'ELG', 'LRG':'LRG', 'QSO':'QSO', 
                        'STD_FSTAR':'STAR', 'STD_BRIGHT':'STAR'}
for m in masks:
    istype = (targets['DESI_TARGET'] & desi_mask.mask(m))!=0
    print(m, np.count_nonzero(istype))
    truth['TRUESPECTYPE'] = np.repeat(dict_truspectype[m], nobj)
    truth['TEMPLATETYPE'] = np.repeat(dict_truetemplatetype[m], nobj)
    truth['MOCKID'][istype] = targets['TARGETID'][istype]

n_unassigned = np.count_nonzero(truth['MOCKID']==0)
print('unassigned', n_unassigned)

mtl = desitarget.mtl.make_mtl(targets)
mtl.meta['EXTNAME'] = 'MTL'

isstd = (targets['DESI_TARGET'] & desi_mask.mask('STD_BRIGHT'))!=0
isstd |= (targets['DESI_TARGET'] & desi_mask.mask('STD_FSTAR'))!=0
print('standards', np.count_nonzero(isstd))
standards = mtl[isstd]


standards.write('standards.fits', overwrite=True)
mtl.write('mtl.fits', overwrite=True)
truth.write('truth.fits', overwrite=True)
