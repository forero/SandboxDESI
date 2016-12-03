What if we split the run in bright/dark-gray? Here are the results.

```bash
forero@edison03:/project/projectdirs/desi/users/forero/datachallenge2017/split
```

### mock creation

| Target | RAM (GB)| time (min) | Filesize (GB) | Target number (M)|
| ------ | ----- | -------- | --- | ------ |
|Standards (SKY, STARS)| 20GB| 12 | stars: 0.8, sky: 1.5 | stars: 10, sky:24 | 
|BRIGHT | 54GB| 40 | 6.4 | bgs: 21, mws: 47 , wd: 0.7| 
|DARK | 42GB| 54 | 4.7 | elg:40, lrg:6, qso:2.5, lya:0.8, badqso:0.9| 

```bash
~/desisim/bin/quicksurvey -O outputlarge/dark/ -T inputlarge/dark/ -f ~/fiberassign/bin/./fiberassign -E inputlarge/ -t inputlarge/template_fiberassign.txt -N 8

 ~/desisim/bin/quicksurvey -O outputlarge/bright/ -T inputlarge/bright/ -f ~/fiberassign/bin/./fiberassign -E inputlarge/ -t inputlarge/template_fiberassign.txt -N 8
 ```
### running quicksurvey

* First epoch
 - DARK: 55GB  (python) / 67GB (fiberassign)
 - BRIGHT: 92GB (python)  / 81GB (fiberassign)

### dark

```bash
~/desisim/bin/quicksurvey -O outputlarge/dark/ -T inputlarge/dark/ -f ~/fiberassign/bin/./fiberassign -E inputlarge/ -t inputlarge/template_fiberassign.txt -N 8

--- Epoch 0 ---
16071 tiles to be included in fiberassign
Fri Dec  2 17:47:57 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 13.32933783531189
DEBUG: calc_priority has 50906026 unobserved targets
0 of 50906026 targets have priority zero, setting N_obs=0.
Fri Dec  2 17:56:02 2016 Finished MTL
Fri Dec  2 17:56:02 2016 Launching fiberassign
...
Sat Dec  3 11:39:27 2016 0 tiles to gather in zcat
Sat Dec  3 11:46:12 2016 Finished zcat
```

### bright

```bash
 ~/desisim/bin/quicksurvey -O outputlarge/bright/ -T inputlarge/bright/ -f ~/fiberassign/bin/./fiberassign -E inputlarge/ -t inputlarge/template_fiberassign.txt -N 8
 
--- Epoch 0 ---
16071 tiles to be included in fiberassign
Fri Dec  2 17:50:21 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 33.11258411407471
DEBUG: calc_priority has 69852026 unobserved targets
0 of 69852026 targets have priority zero, setting N_obs=0.
Fri Dec  2 18:03:08 2016 Finished MTL
Fri Dec  2 18:03:08 2016 Launching fiberassign
Fri Dec  2 19:30:23 2016 Finished fiberassign
Fri Dec  2 19:30:23 2016 2010 tiles to gather in zcat
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact BGS redshift efficiency
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
Fri Dec  2 22:12:30 2016 Finished zcat
--- Epoch 1 ---
14061 tiles to be included in fiberassign
Fri Dec  2 22:12:50 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 32.27236795425415
DEBUG: calc_priority has 61307772 unobserved targets
4664850 of 69852026 targets have priority zero, setting N_obs=0.
/global/common/edison/contrib/desi/conda/conda_3.5-20160829/lib/python3.5/site-packages/astropy/table/column.py:1095: MaskedArrayFutureWarning: setting an item on a masked array which has a shared mask will not copy the mask and also change the original mask array in the future.
Check the NumPy 1.11 release notes for more information.
  ma.MaskedArray.__setitem__(self, index, value)
Fri Dec  2 22:43:06 2016 Finished MTL
Fri Dec  2 22:43:30 2016 Launching fiberassign
Sat Dec  3 00:07:16 2016 Finished fiberassign
Sat Dec  3 00:07:16 2016 2011 tiles to gather in zcat
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact BGS redshift efficiency
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
Sat Dec  3 02:16:50 2016 Finished zcat
--- Epoch 2 ---
12050 tiles to be included in fiberassign
Sat Dec  3 02:17:12 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 33.516958475112915
DEBUG: calc_priority has 53578428 unobserved targets
10714008 of 69852026 targets have priority zero, setting N_obs=0.
Sat Dec  3 02:49:48 2016 Finished MTL
Sat Dec  3 02:49:53 2016 Launching fiberassign
Sat Dec  3 04:01:00 2016 Finished fiberassign
Sat Dec  3 04:01:00 2016 2007 tiles to gather in zcat
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact BGS redshift efficiency
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
Sat Dec  3 06:06:33 2016 Finished zcat
--- Epoch 3 ---
10043 tiles to be included in fiberassign
Sat Dec  3 06:06:55 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 29.287307024002075
DEBUG: calc_priority has 46824595 unobserved targets
17351838 of 69852026 targets have priority zero, setting N_obs=0.
Sat Dec  3 06:39:15 2016 Finished MTL
Sat Dec  3 06:39:19 2016 Launching fiberassign
Sat Dec  3 07:37:56 2016 Finished fiberassign
Sat Dec  3 07:37:56 2016 2010 tiles to gather in zcat
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact BGS redshift efficiency
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
Sat Dec  3 09:33:33 2016 Finished zcat
--- Epoch 4 ---
8033 tiles to be included in fiberassign
Sat Dec  3 09:33:50 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 36.70799922943115
DEBUG: calc_priority has 41100517 unobserved targets
23875339 of 69852026 targets have priority zero, setting N_obs=0.
Sat Dec  3 10:08:12 2016 Finished MTL
Sat Dec  3 10:08:15 2016 Launching fiberassign
Sat Dec  3 10:52:09 2016 Finished fiberassign
Sat Dec  3 10:52:09 2016 2005 tiles to gather in zcat
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact BGS redshift efficiency
WARNING:quickcat.py:225:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:96:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency

Sat Dec  3 12:35:29 2016 Finished zcat

