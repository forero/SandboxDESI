import glob
from desisim.quickcat import quickcat
from astropy.table import Table
fiberassigndir = "/global/cscratch1/sd/forero/DR5FiberAssign/fiberassign/tileresults/"
tile_files = glob.glob(fiberassigndir+"tile_*.fits")
mtl = Table.read("mtl.fits")
truth = Table.read("truth.fits")
zcat = quickcat(tile_files, mtl, truth, perfect=True)
zcat.write("zcat.fits", overwrite=True)
