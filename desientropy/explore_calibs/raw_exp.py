import numpy as np
import matplotlib.pyplot as plt
import fitsio
import os
import glob
import desientropy.compute

def list_raw_exps(date):
    data_path = '/global/cfs/cdirs/desi/spectro/data/'
    desi_raw_exps = glob.glob(os.path.join(data_path, str(date),'*/desi-*.fits.fz'))
    desi_raw_exps.sort()
    return desi_raw_exps

def read_raw_exp(desi_exp_filename):
    fits=fitsio.FITS(desi_exp_filename)
    n_hdu = len(fits)
    a = fits[1]
    header = a.read_header()
    obstype = header['OBSTYPE']
    program = header['PROGRAM']
    expid = header['EXPID']
    
    raw_data = {}
    for i in range(2,4):#n_hdu-1):
        a = fits[i]
        ext_name = a.get_extname()
        print(ext_name)
        raw_data[ext_name] = a.read()
        print(np.shape(raw_data[ext_name]))
    return {'data':raw_data, 'obstype':obstype, 'program':program, 'expid':expid}

def new_data_amp(data_amp, tau=20):
    n_x = np.shape(data_amp)[0]
    n_y = np.shape(data_amp)[1]
    new_n_x = n_x//tau
    new_n_y = n_y//tau
    new_data = np.ones([new_n_x, new_n_y])
    for i in range(new_n_x):
        for j in range(new_n_y):
            new_data[i,j] = np.median(data_amp[i*tau:(i+1)*tau, j*tau:(j+1)*tau])
    return new_data

def compute_raw_exp_entropy(raw_exp_data):
    spectros = list(raw_exp_data['data'].keys())
    print(spectros)
    for spectro in spectros:
        data = raw_exp_data['data'][spectro]
        n_x = np.shape(data)[0]
        n_y = np.shape(data)[1]
        data_amp_A = new_data_amp(data[:n_x//2, :n_y//2])
        data_amp_B = new_data_amp(data[n_x//2:, :n_y//2])
        data_amp_C = new_data_amp(data[:n_x//2, n_y//2:])
        data_amp_D = new_data_amp(data[n_x//2:, n_y//2:])
        
        entropy_A = desientropy.compute.entropy_2d(data_amp_A)
        entropy_B = desientropy.compute.entropy_2d(data_amp_B)
        entropy_C = desientropy.compute.entropy_2d(data_amp_C)
        entropy_D = desientropy.compute.entropy_2d(data_amp_D)

        print(np.shape(data_amp_A), entropy_A)
        print(np.shape(data_amp_B), entropy_B)
        print(np.shape(data_amp_C), entropy_C)
        print(np.shape(data_amp_D), entropy_D)        


        
raw_exp_files = list_raw_exps(20220502)
raw_exp_data = read_raw_exp(raw_exp_files[1])
compute_raw_exp_entropy(raw_exp_data)