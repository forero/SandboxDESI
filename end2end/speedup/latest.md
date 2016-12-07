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
```
