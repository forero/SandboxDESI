# we could move this to desiutil...
from __future__ import absolute_import, division, print_function

import os
import numpy as np

import fitsio
from scipy import constants 

from desitarget.io import check_fitsio_version, iter_files
from desitarget.mock.sample import SampleGMM
from desispec.brick import brickname as get_brickname_from_radec

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

def read_gaussianfield(mock_dir_name, target_name, rand=None, bricksize=0.25,
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

def do_it(comm):
    rank = comm.Get_rank()
    nproc = comm.Get_size()
    
    mock_path = "/project/projectdirs/desi/mocks/GaussianRandomField/v0.0.4/"
    target_name = "ELG"    
    nrows = None
    if rank ==0:
        nrows = countrows_gaussianfield(mock_path, target_name)
        nrows = 100000

    nrows = comm.bcast(nrows, root=0)
    row_start, nrow = dist_uniform(nrows, nproc, rank)    
    print(rank, row_start, nrow)

    rows = range(row_start, row_start+nrow)
    mock_data = read_gaussianfield(mock_path, target_name, rows=rows)
    print(rank, 'RA', len(mock_data['RA']), mock_data['RA'][0])
#    for k in mock_data.keys():
#        print(rank, k, len(mock_data[k]))
#        print(rank, k, mock_data[k])

#    i_buffer = 2
#    rows = range(buffer_size * i_buffer, buffer_size * (i_buffer+1))
#    mock_data = read_gaussianfield(mock_path, target_name, rows=rows)
#    for k in mock_data.keys():
#        print(k, len(mock_data[k]))
#        print(k, mock_data[k])
    return 0

def load_objects(path, comm=None, buffersize=5000):
    """
    Read objects from a file in a buffered way.

    Each process is assigned some contiguous range of bricks.  Then the
    first process reads the file and broadcasts chunks of data.  For
    each chunk, all processes extract out the objects for their assigned
    bricks.

    Args:
        path (str): the path to the file.
        comm (mpi4py.Comm): the communicator to use.
        buffersize (int): the number of objects to read in each chunk.

    Returns:
        a dictionary on each process containing the assigned bricks
            for that process and a list of all the objects for each
            brick.
    """

    nproc = 1
    rank = 0
    if comm is not None:
        nproc = comm.size
        rank = comm.rank

    # Get the total number of objects from the file(s), as well
    # as the total number of bricks (maybe that is known a priori?).

    total_objs = None
    total_bricks = None

    if rank == 0:
        # Open the files and get metadata info (number of HDUs,
        # number of objects, etc)
        total_objs = foo
        total_bricks = bar

    if comm is not None:
        total_objs = comm.bcast(total_objs, root=0)
        total_bricks = comm.bcast(total_bricks, root=0)

    # Compute what our range of bricks is

    brick_start, nbrick = dist_uniform(total_bricks, nproc, rank)

    # Make a list of brick IDs based on the start/number of the bricks.
    # Pretend for now this is just a string, but I know the naming is more
    # complicated.

    brick_list = [ "{:08d}".format(x) for x in range(brick_start, brick_start+nbrick) ]

    # Now read and broadcast the objects in a buffered way, so no process
    # ever stores all objects.

    # This is a dictionary keyed on bricks where the value is a list of
    # objects.
    brick_data = {}

    offset = 0
    nread = buffersize

    while offset < total_bricks:

        # check if we are reading a partial buffer
        if offset + buffersize > total_bricks:
            nread = total_bricks - offset

        buffer = None
        if rank == 0:
            # Here is where the root process would open files, and read
            # the appropriate range of objects.  If there are multiple files,
            # then the bookkeeping could become tedious.  We are reading big
            # chunks of data, it should be OK to open and close the file here.
            buffer = list_of_object_data_from_the_file(offset, nread)
            # buffer now has "nread" number of objects.

        if comm is not None:
            buffer = comm.bcast(buffer, root=0)

        # Now each process grabs the objects in this buffer that are in 
        # their assigned bricks

        for obj in buffer:
            # Find the brick for this object.  Call some function or manually
            # check the RA/DEC here...
            objbrick = get_brick_id(obj.ra, obj.dec) # or something...
            
            if objbrick in brick_list:
                # This is one of our bricks!  Add it to our local dictionary
                brick_data[objbrick].append(obj)

        offset += buffersize

    # Now every process returns a dictionary with its assigned bricks and
    # the relevant objects in a list for each brick.

    return brick_data

from mpi4py import MPI
comm = MPI.COMM_WORLD
do_it(comm)
