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

# list tilefiles already available
fiberassign_tilefiles = glob.glob(os.path.join(args.input_fiberassign,"tile*.fits"))
print(len(fiberassign_tilefiles))

# list sweep files to be used
sweep_files = desitarget.io.list_sweepfiles(args.input_sweep)
n_sweep = len(sweep_files)
print(len(sweep_files))

# list of tiles to be computed
gfa_tiles = np.int_(np.loadtxt(args.input_tiles))
print(len(gfa_tiles))

#load all sweep data
sweep_data = []
#n_sweep = 10
for i in range(n_sweep):
    sweep_file = sweep_files[i]
    sweep_data.append(fitsio.read(sweep_file, columns=['RA', 'DEC', 'FLUX_R']))
    print('Loaded file {} out of {}'.format(i, n_sweep))
all_sweep = np.concatenate(sweep_data, axis=0)

print('There are {:.2f}M targets in the sweeps'.format(len(all_sweep)/1E6))

desi_tiles = desimodel.io.load_tiles()

#find IDs of targets on every individual tile

for tile_id in gfa_tiles:
    ii = desi_tiles['TILEID'] == tile_id
    print('computing TILEID {:05d} on RA {} DEC {}'.format(tile_id, desi_tiles['RA'][ii], desi_tiles['DEC'][ii]))
    
    # select targets in a smaller window centered on tile
    window_ra = 4.0 / np.cos(np.deg2rad(desi_tiles['DEC'][ii]))
    window_dec = 4.0
    print(window_ra, window_dec)
    jj = np.fabs(all_sweep['RA'] - desi_tiles['RA'][ii])<window_ra
    jj = jj | ((all_sweep['RA'] - desi_tiles['RA'][ii] +360.0) < window_ra)
    jj = jj | ((desi_tiles['RA'][ii] - all_sweep['RA'] +360.0) < window_ra)
    jj = jj & (np.fabs(all_sweep['DEC']-desi_tiles['DEC'][ii])<window_dec)
    
    #find GFA targets in the smaller input window
    if np.count_nonzero(jj):
        mini_sweep = all_sweep[jj]
        print('Inside mini_sweep: {:.2f}M targets'.format(len(mini_sweep)/1E6))
        
        targetindices, gfaindices = desimodel.focalplane.on_tile_gfa(tile_id, mini_sweep)
        print('Found {:d} targets on TILEID {:05d}'.format(len(targetindices), tile_id))

        if len(targetindices):
            filename = os.path.join(args.output_dir, "gfa_targets_tile_{:05d}.fits".format(tile_id))        
            print("writing to {}".format(filename))
            a = fitsio.write(filename, mini_sweep[targetindices])
            

