```bash
forero@edison07:/project/projectdirs/desi/users/forero/datachallenge2017/test/quicksurvey_example> date
Tue Dec  6 17:49:22 PST 2016
forero@edison07:/project/projectdirs/desi/users/forero/datachallenge2017/test/quicksurvey_example> pwd
/project/projectdirs/desi/users/forero/datachallenge2017/test/quicksurvey_example
forero@edison07:/project/projectdirs/desi/users/forero/datachallenge2017/test/quicksurvey_example> time ~/desisim/bin/./quicksurvey --output_dir output/bright/ --targets_dir input/bright/ --fiberassign_exec ~/fiberassign/bin/./fiberassign --template_fiberassign input/template_fiberassign.txt --obsconditions input/obsconditions/Benchmark030_001/obslist_all.fits --fiberassign_dates input/fiberassign_dates.txt
--- Epoch 0 ---
16071 tiles to be included in fiberassign
```

```bash
Tue Dec  6 17:50:11 PST 2016
forero@edison08:/project/projectdirs/desi/users/forero/datachallenge2017/test/quicksurvey_example> pwd
/project/projectdirs/desi/users/forero/datachallenge2017/test/quicksurvey_example
forero@edison08:/project/projectdirs/desi/users/forero/datachallenge2017/test/quicksurvey_example> time ~/desisim/bin/./quicksurvey --output_dir output/dark/ --targets_dir input/dark/ --fiberassign_exec ~/fiberassign/bin/./fiberassign --template_fiberassign input/template_fiberassign.txt --obsconditions input/obsconditions/Benchmark030_001/obslist_all.fits --fiberassign_dates input/fiberassign_dates.txt 
--- Epoch 0 ---
16071 tiles to be included in fiberassign
...
--- Epoch 3 ---
1871 tiles to be included in fiberassign
Wed Dec  7 10:07:30 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 24.37631344795227
DEBUG: calc_priority has 20434064 unobserved targets
29783460 of 50908110 targets have priority zero, setting N_obs=0.
Wed Dec  7 10:33:37 2016 Finished MTL
Wed Dec  7 10:33:39 2016 Launching fiberassign
Wed Dec  7 10:44:21 2016 Finished fiberassign
Suggested but does not exist output/dark/tmp/fiberassign/tile_24104.fits
Wed Dec  7 10:44:22 2016 1636 tiles to gather in zcat
Wed Dec  7 10:44:22 2016 starting quickcat
Wed Dec  7 10:44:22 2016 QC Reading 1636 tiles
Wed Dec  7 10:45:09 2016 QC Trimming truth to just observed targets
Wed Dec  7 10:46:01 2016 QC Constructing new redshift catalog
Wed Dec  7 10:46:01 2016 QC Adding ZERR and ZWARN
```
