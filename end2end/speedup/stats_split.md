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
 - BRIGHT: 92GB (python)  / 
 - DARK: 55GB  (python) / 65GB (fiberassign)

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
 
```
