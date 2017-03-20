# we could move this to desiutil...
from __future__ import absolute_import, division, print_function

import os
import numpy as np

import fitsio
from scipy import constants 

from desitarget.io import check_fitsio_version, iter_files
from desitarget.mock.sample import SampleGMM
from desispec.brick import brickname as get_brickname_from_radec

import os
from time import time

import yaml
import numpy as np
from astropy.io import fits
from astropy.table import Table, Column, vstack

from desispec.io.util import fitsheader, write_bintable
from desispec.brick import brickname as get_brickname_from_radec

import desitarget.mock.io as mockio
import desitarget.mock.selection as mockselect
from desitarget.mock.spectra import MockSpectra
from desitarget.internal import sharedmem
from desitarget.targetmask import desi_mask, bgs_mask, mws_mask


from desispec.log import get_logger, DEBUG
from desispec.parallel import dist_uniform

log = get_logger(DEBUG)

def countrows_gaussianfield(mock_dir_name, target_name):
    if target_name == 'SKY':
        mockfile = mock_dir_name
        columns = ['RA', 'DEC']
    else:
        from pathlib import Path
        f = Path(mock_dir_name)
        if f.is_file():
            mockfile = mock_dir_name
        else:
            mockfile = os.path.join(mock_dir_name, '{}.fits'.format(target_name.upper()))
    nrows = fitsio.FITS(mockfile)[1].get_nrows()
    return nrows

def read_gaussianfield(mock_dir_name, target_name,
               bounds=None, magcut=None, rows=None):
    if target_name == 'SKY':
        mockfile = mock_dir_name
        columns = ['RA', 'DEC']
    else:
        from pathlib import Path
        f = Path(mock_dir_name)
        if f.is_file():
            mockfile = mock_dir_name
        else:
            mockfile = os.path.join(mock_dir_name, '{}.fits'.format(target_name.upper()))

        columns = ['RA', 'DEC', 'Z_COSMO', 'DZ_RSD']        
    try:
        os.stat(mockfile)
    except:
        log.fatal('Mock file {} not found!'.format(mockfile))
        raise IOError

    if rows is None:
        data = fitsio.read(mockfile, columns=columns, upper=True)
    else:
        log.warning('Reading a subset')
        data = fitsio.read(mockfile, columns=columns, upper=True, rows=rows)
    
    ra = data['RA'].astype('f8') % 360.0 # enforce 0 < ra < 360
    dec = data['DEC'].astype('f8')
    if 'Z_COSMO' in data.dtype.names:
        zz = (data['Z_COSMO'].astype('f8') + data['DZ_RSD'].astype('f8')).astype('f4')
    else:
        zz = np.zeros_like(ra).astype('f4')

    out = {'RA': ra, 'DEC': dec, 'Z': zz}
    return out

def add_seed(input, rand):
    nobj = len(input['RA'])
    seed = rand.randint(2**32, size=nobj)
    input.update({'SEED':seed})

def add_GMM_gaussianfield(input, target_name, rand):
    if target_name == 'SKY':
        input.update({'TRUESPECTYPE': 'SKY', 'TEMPLATETYPE': 'SKY', 'TEMPLATESUBTYPE': ''})
    else:
        nobj = len(input['RA'])
        log.info('Sampling from Gaussian mixture model.')
        GMM = SampleGMM(random_state=rand)
        mags = GMM.sample(target_name, nobj) # [g, r, z, w1, w2, w3, w4]

        input.update({'GR': mags[:, 0]-mags[:, 1], 'RZ': mags[:, 1]-mags[:, 2],
                    'RW1': mags[:, 1]-mags[:, 3], 'W1W2': mags[:, 3]-mags[:, 4]})
    
        if target_name == 'ELG':
            """Selected in the r-band with g-r, r-z colors."""
            vdisp = 10**rand.normal(1.9, 0.15, nobj)
            input.update({'TRUESPECTYPE': 'GALAXY', 'TEMPLATETYPE': 'ELG', 'TEMPLATESUBTYPE': '',
                        'VDISP': vdisp, 'MAG': mags[:, 1], 'FILTERNAME': 'decam2014-r'})

        elif target_name == 'LRG':
            """Selected in the z-band with r-z, r-W1 colors."""
            vdisp = 10**rand.normal(2.3, 0.1, nobj)
            out.update({'TRUESPECTYPE': 'GALAXY', 'TEMPLATETYPE': 'LRG', 'TEMPLATESUBTYPE': '',
                        'VDISP': vdisp, 'MAG': mags[:, 2], 'FILTERNAME': 'decam2014-z'})
            
        elif target_name == 'QSO':
            """Selected in the r-band with g-r, r-z, and W1-W2 colors."""
            input.update({'TRUESPECTYPE': 'QSO', 'TEMPLATETYPE': 'QSO', 'TEMPLATESUBTYPE': '',
                        'MAG': mags[:, 1], 'FILTERNAME': 'decam2014-r'})
            
        else:
            log.fatal('Unrecognized target type {}!'.format(target_name))
            raise ValueError


def do_it(comm):
    rank = comm.Get_rank()
    nproc = comm.Get_size()
    
    mock_path = "/project/projectdirs/desi/mocks/GaussianRandomField/v0.0.4/"
    target_name = "ELG"    
    mockformat = "gaussianfield"
    nrows = None
    rand = np.random.RandomState()
    Spectra = MockSpectra(rand=rand)

    if rank ==0:
#        nrows = countrows_gaussianfield(mock_path, target_name)
        nrows = 200 * nproc

    nrows = comm.bcast(nrows, root=0)
    row_start, nrow = dist_uniform(nrows, nproc, rank)    
    print(rank, row_start, nrow)

    rows = range(row_start, row_start+nrow)
    mock_data = read_gaussianfield(mock_path, target_name, rows=rows)
    add_GMM_gaussianfield(mock_data, target_name, rand)
    add_seed(mock_data, rand=rand)
    trueflux, meta = getattr(Spectra, target_name.lower())(mock_data, mockformat=mockformat)

    print(rank, 'RA', len(mock_data['RA']), mock_data['RA'][0])

    return 0

from mpi4py import MPI
comm = MPI.COMM_WORLD
do_it(comm)
