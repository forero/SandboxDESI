import numpy as np
import fitsio

target_filename = "090000-unique_targ.fits"
data_main = fitsio.read(target_filename)

fba_main = fitsio.read("fiberassign-090000.fits")
fiber_id = (fba_main['FIBER']%500)

for m in range(9):
    ii = (fiber_id & (2**m))!=0
    tid_to_include = fba_main['TARGETID'][ii]    
    tin = np.isin(data_main['TARGETID'], tid_to_include)
#    print('{} targets in the original file'.format(len(data_main['TARGETID'])))

    new_data = data_main[tin]
#    print('{} targets in the new file'.format(len(new_data['TARGETID'])))

    new_filename = target_filename.replace("targ", "unique_targ_m_{:02d}".format(m))
    fitsio.write(new_filename, new_data)
    print(new_filename)
    print()
    #print(i,np.count_nonzero(fba_main['DEVICE_LOC']==i))

# final parity check
m = 0
ii = ~((fiber_id & (2**m))!=0)
tid_to_include = fba_main['TARGETID'][ii]
tin = np.isin(data_main['TARGETID'], tid_to_include)
new_data = data_main[tin]
m = 9
new_filename = target_filename.replace("targ", "unique_targ_m_{:02d}".format(m))
fitsio.write(new_filename, new_data)
print(new_filename)
print()