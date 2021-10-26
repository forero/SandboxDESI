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
fiberflats = glob.glob(os.path.join(data_path, "2021*/fiberflatnight-z0-*.fits"))
fiberflats.sort()

for camera in ['b', 'r', 'z']:
    for petal in range(2):
        camera_petal = camera+str(petal)
        
        for f in fiberflats[:2]:
            fflat = f.replace('z0', camera_petal)
            print(fflat)
            fflat_data = read_fflat(fflat)
            pdistro = ient.compute_probability_distribution(fflat_data)
            entropy = ient.compute_entropy(pdistro)
            print(entropy)