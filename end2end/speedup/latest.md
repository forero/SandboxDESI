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
--- Epoch 4 ---
234 tiles to be included in fiberassign
Wed Dec  7 12:16:54 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 24.599448204040527
DEBUG: calc_priority has 14491426 unobserved targets
35839006 of 50908110 targets have priority zero, setting N_obs=0.
Wed Dec  7 12:43:03 2016 Finished MTL
Wed Dec  7 12:43:05 2016 Launching fiberassign
Wed Dec  7 12:48:27 2016 Finished fiberassign
Suggested but does not exist output/dark/tmp/fiberassign/tile_24957.fits
Suggested but does not exist output/dark/tmp/fiberassign/tile_24100.fits
Suggested but does not exist output/dark/tmp/fiberassign/tile_24081.fits
Suggested but does not exist output/dark/tmp/fiberassign/tile_24116.fits
Suggested but does not exist output/dark/tmp/fiberassign/tile_24139.fits
Suggested but does not exist output/dark/tmp/fiberassign/tile_24129.fits
Suggested but does not exist output/dark/tmp/fiberassign/tile_24146.fits
Suggested but does not exist output/dark/tmp/fiberassign/tile_24135.fits
Suggested but does not exist output/dark/tmp/fiberassign/tile_24084.fits
Wed Dec  7 12:48:27 2016 225 tiles to gather in zcat
Wed Dec  7 12:48:27 2016 starting quickcat
Wed Dec  7 12:48:27 2016 QC Reading 225 tiles
Wed Dec  7 12:48:33 2016 QC Trimming truth to just observed targets
Wed Dec  7 12:49:27 2016 QC Constructing new redshift catalog
Wed Dec  7 12:49:27 2016 QC Adding ZERR and ZWARN
WARNING:quickcat.py:226:get_redshift_efficiency: using default redshift efficiency of 0.98 for STAR
WARNING:quickcat.py:97:get_zeff_obs: No model for how observing conditions impact STAR redshift efficiency
Wed Dec  7 12:50:31 2016 QC Adding NUMOBS column
Wed Dec  7 12:50:48 2016 QC Merging previous zcat
Wed Dec  7 12:52:05 2016 QC done
Wed Dec  7 12:52:05 2016 writing zcat
Wed Dec  7 12:58:56 2016 Finished zcat

real	1142m58.388s
user	1098m28.979s
sys	114m27.477s
```

```bash
forero@edison10:/project/projectdirs/desi/users/forero/datachallenge2017/test/quicksurvey_example> date
Wed Dec  7 16:36:07 PST 2016
forero@edison10:/project/projectdirs/desi/users/forero/datachallenge2017/test/quicksurvey_example> time ~/desisim/bin/./quicksurvey --output_dir output/brightepochs/ --targets_dir input/bright/ --fiberassign_exec ~/fiberassign/bin/./fiberassign --template_fiberassign input/template_fiberassign.txt --n_epochs 3 --epochs_dir input/bright/
```
