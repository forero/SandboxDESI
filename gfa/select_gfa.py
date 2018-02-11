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
n_sweep = len(sweep_files)
print(len(sweep_files))

# list of tiles to be computed
gfa_tiles = np.int_(np.loadtxt(args.input_tiles))
print(len(gfa_tiles))

#load all sweep data
sweep_data = []
n_sweep = 10
for i in range(n_sweep):
    sweep_file = sweep_files[i]
    sweep_data.append(fitsio.read(sweep_file, columns=['RA', 'DEC', 'FLUX_R']))
all_sweep = np.concatenate(sweep_data, axis=0)

print('There are {:.2f}M targets in the sweeps'.format(len(all_sweep)/1E6))

desi_tiles = desimodel.io.load_tiles()

#find IDs of targets on every individual tile
all_targetindices = dict()
for tile_id in gfa_tiles:
    ii = desi_tiles['TILEID'] == tile_id
    print('computing TILEID {:05d} on RA {} DEC {}'.format(tile_id, desi_tiles['RA'][ii], desi_tiles['DEC'][ii]))
    targetindices, gfaindices = desimodel.focalplane.on_tile_gfa(tile_id, all_sweep)
    all_targetindices[tile_id] = targetindices
    print('Found {:05d} targets on TILEID {:d}'.format(len(targetindices), tile_id))
