import numpy as np
import matplotlib.pyplot as plt
import fitsio
import os
import glob
import desientropy.compute
import pandas as pd

def list_raw_exps(date):
    data_path = '/global/cfs/cdirs/desi/spectro/data/'
    desi_raw_exps = glob.glob(os.path.join(data_path, str(date),'*/desi-*.fits.fz'))
    desi_raw_exps.sort()
    return desi_raw_exps

def read_raw_exp(desi_exp_filename):
    print('reading ', desi_exp_filename)
    fits=fitsio.FITS(desi_exp_filename)
    n_hdu = len(fits)
    a = fits[1]
    header = a.read_header()
    obstype = header['OBSTYPE']
    program = header['PROGRAM']
    expid = header['EXPID']
    night = header['NIGHT']
    
    raw_data = {}
    for i in range(2,4):#n_hdu-1):
        a = fits[i]
        ext_name = a.get_extname()
        raw_data[ext_name] = a.read()
    return {'DATA':raw_data, 'OBSTYPE':obstype, 'PROGRAM':program, 'EXPID':expid, 'NIGHT':night}

def new_data_amp(data_amp, tau=30):
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
    summary = {}
    summary['SPECTRO'] = []
    summary['AMP'] = []
    summary['EXPID'] = []
    summary['NIGHT'] = []
    summary['PROGRAM'] = []
    summary['OBSTYPE'] = []
    summary['H'] = []

    spectros = list(raw_exp_data['DATA'].keys())
    print('computing for expid', raw_exp_data['EXPID'])
    for spectro in spectros:
        print('\t spectro:', spectro)
        data = raw_exp_data['DATA'][spectro]
        n_x = np.shape(data)[0]
        n_y = np.shape(data)[1]
        
        amps = ['A', 'B', 'C', 'D']
        data_amp = list(range(len(amps)))
        data_amp[0] = new_data_amp(data[:n_x//2, :n_y//2])
        data_amp[1] = new_data_amp(data[n_x//2:, :n_y//2])
        data_amp[2] = new_data_amp(data[:n_x//2, n_y//2:])
        data_amp[3] = new_data_amp(data[n_x//2:, n_y//2:])
        
        entropy = list(range(len(amps)))
        for i in range(len(amps)):
            entropy[i] = desientropy.compute.entropy_2d(data_amp[i])
            
        for i in range(len(amps)):
            summary['SPECTRO'].append(spectro)
            summary['AMP'].append(amps[i])
            summary['H'].append(entropy[i])
            for j in ['EXPID', 'PROGRAM', 'OBSTYPE', 'NIGHT']:
                summary[j].append(raw_exp_data[j])
    #print(summary)
    entropy_df = pd.DataFrame.from_dict(summary)
    filename = 'entropy_raw_exp_{}_{:08d}.csv'.format(raw_exp_data['NIGHT'], raw_exp_data['EXPID'])    
    entropy_df.to_csv(filename)
    return 
        
def summary_entropy_night(date):
    raw_exp_files = list_raw_exps(date)
    n = len(raw_exp_files)
    for i in range(n):
        raw_exp_data = read_raw_exp(raw_exp_files[i])
        compute_raw_exp_entropy(raw_exp_data)
        del raw_exp_data
        
summary_entropy_night(20220502)