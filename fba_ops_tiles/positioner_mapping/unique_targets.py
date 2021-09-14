import numpy as np
import fitsio
from collections import Counter

target_filename = "090000-targ.fits"
data_main = fitsio.read(target_filename)

print('{} targets in the original file'.format(len(data_main['TARGETID'])))
# cut-off the faint targets
ii = data_main['GAIA_PHOT_G_MEAN_MAG']<=19
data_main = data_main[ii]
print('{} targets after the magnitude cut'.format(len(data_main['TARGETID'])))


fba_potential = fitsio.read("fiberassign-090000.fits", ext="POTENTIAL_ASSIGNMENTS")

# only include targets that were potential targets to a single fiber
count_potential = Counter(fba_potential['TARGETID'])

tid_to_include = []
for k in count_potential.keys():
    if (count_potential[k]==1) and (k>0):
        tid_to_include.append(k)



tin = np.isin(data_main['TARGETID'], tid_to_include)
print('{} targets in the original file'.format(len(data_main['TARGETID'])))

new_data = data_main[tin]
print('{} targets in the new file'.format(len(new_data['TARGETID'])))

new_filename = target_filename.replace("targ", "unique_targ")
fitsio.write(new_filename, new_data)
