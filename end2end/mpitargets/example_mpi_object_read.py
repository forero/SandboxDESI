# Demo of buffered MPI distribution of objects by brick by @tkisner
# https://gist.github.com/tskisner/ebf41a77264dc721c9c098d83eb11f37

# we could move this to desiutil...
from desispec.parallel import dist_uniform


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
