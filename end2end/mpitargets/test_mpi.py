from mpi4py import MPI
import multiprocessing
import numpy as np

bricks = 60
c = list(range(bricks))
d = []


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size= comm.Get_size()

n_per_proc = bricks//size
min_i = rank * n_per_proc
max_i = (rank + 1) * n_per_proc
if (rank==(size-1)):
    max_i = bricks

print(rank, min_i, max_i)
for i in range(min_i, max_i):
    d.append(rank)

e = comm.gather(d, root=0)


print(e, rank)

