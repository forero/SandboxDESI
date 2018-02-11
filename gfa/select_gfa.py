import desimodel.focalplane
import desitarget.io
import fitsio
import numpy as np
import desimodel.io
import desimodel.footprint
import matplotlib.pyplot as plt
import glob
import os.path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output_dir', help='Path to write the outputs', type=str)
parser.add_argument('-s', '--input_sweep', help='Path to the sweep files', type=str)
parser.add_argument('-f', '--input_fiberassign', help='Path to fiberassign output files', type=str)
parser.add_argument('-t', '--input_tiles', help='Input file with the tileid gfa files to be computed', type=str)

args = parser.parse_args()

# list tilefiles
fiberassign_tilefiles = glob.glob(os.path.join(args.input_fiberassign,"tile*.fits"))
print(len(fiberassign_tilefiles))

# list sweep files
sweep_files = desitarget.io.list_sweepfiles(args.input_sweep)
print(len(sweep_files))

# list of tiles to be computed
gfa_tiles = np.loadtxt(args.input_tiles)
print(len(gfa_tiles))


