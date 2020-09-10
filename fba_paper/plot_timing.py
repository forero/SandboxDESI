import numpy as np
import matplotlib.pyplot as plt

timing = {}
timing['D'] = np.loadtxt("timing/timing_mtl_cut_D_tiles_cut_D.dat")
timing['C'] = np.loadtxt("timing/timing_mtl_cut_C_tiles_cut_C.dat")
timing['B'] = np.loadtxt("timing/timing_mtl_cut_B_tiles_cut_B.dat")


plt.figure()
plt.plot(timing['B'][:,0]/timing['B'][-1,0], timing['B'][:,1]/timing['B'][-1,1])
plt.plot(timing['C'][:,0]/timing['C'][-1,0], timing['C'][:,1]/timing['C'][-1,1])
plt.plot(timing['D'][:,0]/timing['D'][-1,0], timing['D'][:,1]/timing['D'][-1,1])
plt.xlabel("Time [seconds]")
plt.ylabel("Memory [GB]")
plt.savefig("timing.pdf")