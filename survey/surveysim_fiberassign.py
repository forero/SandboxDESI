# coding: utf-8

import os
import sys
from astropy.table import Table
from desisurvey.progress import Progress
import desimodel.io
import numpy as np
import datetime
import yaml

def compute_fiberassign_dates(exposurefile):
    """
    Computes the dates to read fiberassign from the data in a 'exposures' files.
    
    Args:
        exposurefile (str):
        Name of the file with 'exposures' data
    Return:
        fiberassign_dates_run (list):
        List of string dates where fiberassign should be run.
    """
    desisurvey_path = os.getenv('DESISURVEY_OUTPUT')
    exposures = Table.read(exposurefile)
    expdates = []
    for n in exposures['night']:
        a = datetime.datetime.strptime(n, "%Y-%m-%d")
        expdates.append(a.date())
    expdates = np.array(expdates)

    # compute the dates for fiberassign
    progress = Table.read(os.path.join(desisurvey_path,'progress.fits'))
    fiberassign_dates = np.sort(list(set(progress['available'])))
    fiberassign_dates = fiberassign_dates[fiberassign_dates>0]
    
    #load the first date of the survey
    survey_config = os.path.join(desisurvey_path,'config.yaml')
    with open(survey_config, 'r') as pfile:
        params = yaml.load(pfile)
    pfile.close()
    first_day = params['first_day']
    last_day = params['last_day']
    print(first_day, last_day)
    
    #compute the dates to run fiberassign to be sure that there is at least one exposure there
    fiberassign_dates_run = []
    one_day = datetime.timedelta(days=1)
    initial_day = first_day 
    for d in fiberassign_dates:
        final_day = first_day + d * one_day
        ii = (expdates > initial_day) & (expdates<=final_day)
        n_in = np.count_nonzero(ii)
        if n_in>0:
            print(initial_day, final_day, n_in)
            fiberassign_dates_run.append(initial_day.strftime("%Y-%m-%d"))
            initial_day = final_day
    return fiberassign_dates_run

desisurvey_path = os.getenv('DESISURVEY_OUTPUT')

if desisurvey_path is None:
    print('Environment variable DESISURVEY_OUTPUT is not set')
else:
    print('Environment variable DESISURVEY_OUTPUT set to {}'.format(desisurvey_path))
    Progress(restore='progress.fits').get_exposures().write(os.path.join(desisurvey_path,'exposures.fits'), overwrite=True)
    
    explist = Table.read(os.path.join(desisurvey_path,'exposures.fits'))

    # separate the exposures for dark and bright programs
    isbright = explist['pass'] > 4 
    isgray = explist['pass'] == 4
    isdark = explist['pass'] < 4
    
    exposurefile_bright = os.path.join(desisurvey_path,'exposures_bright.fits')
    Table(explist[isbright]).write(exposurefile_bright, overwrite=True)

    exposurefile_dark = os.path.join(desisurvey_path,'exposures_dark.fits')
    Table(explist[~isbright]).write(exposurefile_dark, overwrite=True)
    

    fiberdatesfile_bright = os.path.join(desisurvey_path, 'fiberassign_dates_bright.txt')
    fiberassign_dates_bright = compute_fiberassign_dates(exposurefile_bright)
    f = open(fiberdatesfile_bright, 'w')
    for d in fiberassign_dates_bright:
        f.write(d+"\n")
    f.close()
    
    fiberdatesfile_dark = os.path.join(desisurvey_path, 'fiberassign_dates_dark.txt')
    fiberassign_dates_dark = compute_fiberassign_dates(exposurefile_dark)
    f = open(fiberdatesfile_dark, 'w')
    for d in fiberassign_dates_dark:
        f.write(d+"\n")
    f.close()