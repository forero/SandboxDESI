import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
MEDIUM_SIZE = 30
SMALL_SIZE = 22
SSSMALL_SIZE = 16

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)

ntargets = pd.read_csv("sizes/targets_dark_north.dat").set_index('cut')
nsky = pd.read_csv("sizes/sky_dark_north.dat").set_index('cut')
ntiles = pd.read_csv("sizes/tiles_dark_north.dat").set_index('cut')
print(ntiles)

timing = {}
cuts = ['B', 'C', 'D', 'E']
max_time = np.ones(len(cuts))
max_ram = np.ones(len(cuts))
for i, cut in enumerate(cuts):
    timing[cut] = np.loadtxt("timing/timing_mtl_cut_{}_tiles_cut_{}.dat".format(cut,cut))
    max_time[i] = np.max(timing[cut][:,0])
    max_ram[i] = np.max(timing[cut][:,1])

n_targets = np.array(ntargets.loc[cuts, 'ntargets'])
n_sky = np.array(nsky.loc[cuts, 'nsky'])
n_tiles = np.array(ntiles.loc[cuts, 'ntiles'])
n_targets_sky  = n_targets + n_sky
x_targets = np.linspace(n_targets.min(), n_targets.max(), 100)
x_targets_sky = np.linspace(n_targets.min()+n_sky.min(), n_targets.max()+n_sky.max(), 100)


plt.figure()
plt.scatter(n_targets_sky, max_time/60, label='NERSC')
plt.plot(x_targets_sky, x_targets_sky*max_time[-1]/n_targets_sky[-1]/60, label='linear scaling')
plt.loglog()
plt.legend()
plt.xlabel("N targets")
plt.ylabel("Running time [minutes]")
plt.savefig("ntargets_time_scaling.pdf", bbox_inches='tight')


plt.figure()
plt.scatter(n_targets_sky, max_ram, label='NERSC')
plt.plot(x_targets_sky, x_targets_sky*max_ram[-1]/(n_targets_sky[-1]), label='linear scaling')
plt.loglog()
plt.legend()
plt.xlabel("N targets")
plt.ylabel("Peak RAM [GB]")
plt.savefig("ntargets_ram_scaling.pdf", bbox_inches='tight')

plt.figure()
plt.scatter(cuts, n_targets, marker='^', label='Science')
plt.scatter(cuts, n_sky, marker='v', label='Sky')
plt.semilogy()
plt.legend()
plt.xlabel("Experiment Name")
plt.ylabel("Number of Targets")
plt.savefig("runs.pdf", bbox_inches='tight')


plt.figure()
for cut in cuts:
    plt.plot(timing[cut][:,0]/timing[cut][-1,0], timing[cut][:,1]/np.max(timing[cut][:,1]), 
                             label='N targets = {:.1e}'.format(ntargets.loc[cut, 'ntargets']))
    
plt.legend()
plt.xlim([0,1])
plt.ylim([0,1.02])
plt.xlabel("Normalized Running Time")
plt.ylabel("Normalizd RAM Usage")
plt.savefig("normalized_timing.pdf", bbox_inches='tight')
