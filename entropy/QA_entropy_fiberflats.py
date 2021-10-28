#QA on the calibration fiberflats

import numpy as np
import matplotlib.pyplot as plt
import fitsio
import glob
import os
import image_entropy as ient

def read_fflat(filename):
    h = fitsio.FITS(filename)
    fflat_data = h["FIBERFLAT"].read() 
    return fflat_data

data_path = "/global/cfs/cdirs/desi/spectro/redux/daily/calibnight/"
fiberflats = glob.glob(os.path.join(data_path, "20211*/fiberflatnight-z0-*.fits"))
fiberflats.sort()


outfile = open("calibnight_entropy.csv","w")
outfile.write("NIGHT,CAMERA,PETAL,ENTROPY\n")
outfile.close()

for f in fiberflats:
    date = f.split('/')[-2]
    for petal in range(10):
        for camera in ['b', 'r', 'z']:
            camera_petal = camera+str(petal)
            fflat = f.replace('z0', camera_petal)
            print(fflat)
            try:
                fflat_data = read_fflat(fflat)
                pdistro = ient.compute_probability_distribution_2D(fflat_data, n_stride=10)
                entropy = ient.compute_entropy(pdistro)
            
                out = "{},{},{},{}\n".format(date, camera, petal, entropy)
                print(out)
                outfile = open("calibnight_entropy.csv","a")
                outfile.write(out)
                outfile.close()
            except:
                pass
