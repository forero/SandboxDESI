```bash
forero@edison09:/project/projectdirs/desi/users/forero/datachallenge2017/fastsplit/quicksurvey_example> ~/desisim/bin/quicksurvey -O outputlarge/dark/ -T inputlarge/dark/ -f ~/fiberassign/bin/./fiberassign -E inputlarge/dark/ -t inputlarge/template_fiberassign.txt -N 5
--- Epoch 0 ---
10043 tiles to be included in fiberassign
Sat Dec  3 14:49:18 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 21.63566780090332
DEBUG: calc_priority has 50906026 unobserved targets
0 of 50906026 targets have priority zero, setting N_obs=0.
Sat Dec  3 14:58:39 2016 Finished MTL
Sat Dec  3 14:58:39 2016 Launching fiberassign
Sat Dec  3 15:39:59 2016 Finished fiberassign
Sat Dec  3 15:39:59 2016 2010 tiles to gather in zcat
/global/homes/f/forero/desisim/py/desisim/quickcat.py:186: RuntimeWarning: divide by zero encountered in log10
  r_mag = 22.5 - 2.5*np.log10(true_rflux)
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
Sat Dec  3 17:55:15 2016 Finished zcat
--- Epoch 1 ---
8033 tiles to be included in fiberassign
Sat Dec  3 17:55:33 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 24.761712789535522
DEBUG: calc_priority has 42312353 unobserved targets
5480481 of 50906026 targets have priority zero, setting N_obs=0.
/global/common/edison/contrib/desi/conda/conda_3.5-20160829/lib/python3.5/site-packages/astropy/table/column.py:1095: MaskedArrayFutureWarning: setting an item on a masked array which has a shared mask will not copy the mask and also change the original mask array in the future.
Check the NumPy 1.11 release notes for more information.
  ma.MaskedArray.__setitem__(self, index, value)
Sat Dec  3 18:17:09 2016 Finished MTL
Sat Dec  3 18:17:13 2016 Launching fiberassign
Sat Dec  3 18:54:08 2016 Finished fiberassign
Sat Dec  3 18:54:08 2016 2011 tiles to gather in zcat
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
Sat Dec  3 21:07:24 2016 Finished zcat
--- Epoch 2 ---
6022 tiles to be included in fiberassign
Sat Dec  3 21:07:37 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 14.207956075668335
DEBUG: calc_priority has 35588249 unobserved targets
10689743 of 50906026 targets have priority zero, setting N_obs=0.
Sat Dec  3 21:28:28 2016 Finished MTL
Sat Dec  3 21:28:31 2016 Launching fiberassign
Sat Dec  3 21:57:17 2016 Finished fiberassign
Sat Dec  3 21:57:17 2016 2007 tiles to gather in zcat
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
Sun Dec  4 00:31:54 2016 Finished zcat
--- Epoch 3 ---
4015 tiles to be included in fiberassign
Sun Dec  4 00:32:44 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 24.927589178085327
DEBUG: calc_priority has 30039141 unobserved targets
16781782 of 50906026 targets have priority zero, setting N_obs=0.
Sun Dec  4 00:57:31 2016 Finished MTL
Sun Dec  4 00:57:40 2016 Launching fiberassign
Sun Dec  4 01:17:34 2016 Finished fiberassign
Sun Dec  4 01:17:34 2016 2010 tiles to gather in zcat
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
Sun Dec  4 03:45:41 2016 Finished zcat
--- Epoch 4 ---
2005 tiles to be included in fiberassign
Sun Dec  4 03:45:54 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 22.739306211471558
DEBUG: calc_priority has 24158480 unobserved targets
24038012 of 50906026 targets have priority zero, setting N_obs=0.
Sun Dec  4 04:09:33 2016 Finished MTL
Sun Dec  4 04:09:33 2016 Launching fiberassign
Sun Dec  4 04:21:03 2016 Finished fiberassign
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24084.fits
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24100.fits
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24104.fits
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24116.fits
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24121.fits
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24129.fits
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24135.fits
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24139.fits
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24146.fits
Suggested but does not exist outputlarge/dark/tmp/fiberassign/tile_24957.fits
Sun Dec  4 04:21:03 2016 1995 tiles to gather in zcat
Sun Dec  4 07:22:48 2016 Finished zcat
```

```bash

forero@edison03:/project/projectdirs/desi/users/forero/datachallenge2017/fastsplit/quicksurvey_example> ~/desisim/bin/quicksurvey -O outputlarge/bright/ -T inputlarge/bright/ -f ~/fiberassign/bin/./fiberassign -E inputlarge/bright/ -t inputlarge/template_fiberassign.txt -N 3
--- Epoch 0 ---
6028 tiles to be included in fiberassign
Sat Dec  3 14:51:44 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 30.601342916488647
DEBUG: calc_priority has 69852026 unobserved targets
0 of 69852026 targets have priority zero, setting N_obs=0.
Sat Dec  3 15:04:07 2016 Finished MTL
Sat Dec  3 15:04:07 2016 Launching fiberassign
Sat Dec  3 15:31:42 2016 Finished fiberassign
Sat Dec  3 15:31:42 2016 2007 tiles to gather in zcat
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact BGS redshift efficiency
Sat Dec  3 17:56:42 2016 Finished zcat
--- Epoch 1 ---
4021 tiles to be included in fiberassign
Sat Dec  3 17:57:23 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 32.882493019104004
DEBUG: calc_priority has 60921635 unobserved targets
7073608 of 69852026 targets have priority zero, setting N_obs=0.
/global/common/edison/contrib/desi/conda/conda_3.5-20160829/lib/python3.5/site-packages/astropy/table/column.py:1095: MaskedArrayFutureWarning: setting an item on a masked array which has a shared mask will not copy the mask and also change the original mask array in the future.
Check the NumPy 1.11 release notes for more information.
  ma.MaskedArray.__setitem__(self, index, value)
Sat Dec  3 18:29:50 2016 Finished MTL
Sat Dec  3 18:29:52 2016 Launching fiberassign
Sat Dec  3 18:51:37 2016 Finished fiberassign
Sat Dec  3 18:51:38 2016 2011 tiles to gather in zcat
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact BGS redshift efficiency
Sat Dec  3 21:12:07 2016 Finished zcat
--- Epoch 2 ---
2010 tiles to be included in fiberassign
Sat Dec  3 21:12:51 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 35.98475503921509
DEBUG: calc_priority has 52162201 unobserved targets
13852505 of 69852026 targets have priority zero, setting N_obs=0.
Sat Dec  3 21:45:04 2016 Finished MTL
Sat Dec  3 21:45:06 2016 Launching fiberassign
Sat Dec  3 21:57:05 2016 Finished fiberassign
Sat Dec  3 21:57:05 2016 2010 tiles to gather in zcat
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact BGS redshift efficiency
Sun Dec  4 00:20:09 2016 Finished zcat

```
