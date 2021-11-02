import numpy as np
import matplotlib.pyplot as plt
import fitsio
import glob
import os
import image_entropy as ient


def read_desi_exposure(filename, camera='b', petal=0):
    try:
        exp_data = fitsio.read(filename, ext=camera+str(petal)) 
        header = fitsio.read(filename, header=True)
        flavor = header[1]["FLAVOR"]
        return exp_data, flavor
    except:
        return None, None
data_path = "/global/cfs/cdirs/desi/spectro/data/"

exposures = glob.glob(os.path.join(data_path, "2021101*/*/desi*.fits.fz"))
exposures.sort()
print(exposures)

outname = "entropy_exposures_2021101.csv"
outfile = open(outname,"w")
outfile.write("NIGHT,EXPID,FLAVOR,CAMERA,PETAL,ENTROPY\n")
outfile.close()

print(len(exposures))
for exp_file in exposures:
    night = exp_file.split('/')[-3]
    expid = int(exp_file.split('/')[-2])
    
    for camera in ['b', 'r', 'z']:
        for petal in range(10):            
            data, flavor = read_desi_exposure(exp_file, camera=camera, petal=petal)
            entropy = -1
            if data is not None:
                p = ient.compute_probability_distribution_2D(data, n_stride=20)
                entropy = ient.compute_entropy(p)
                
            print(night, expid, flavor, camera, petal, entropy, np.shape(data))
            out = "{},{},{},{},{},{}\n".format(night, expid, flavor, camera, petal, entropy)
            print(out)
            outfile = open(outname,"a")
            outfile.write(out)
            outfile.close()




