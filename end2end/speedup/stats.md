Stats for 'select_mock_targets' run on separate files

### Dark

Setup

```bash
forero@edison06:/project/projectdirs/desi/users/forero/quicksurvey_example> time ~/desitarget/bin/select_mock_targets -c input/mock_dark.yaml  -O input/dark/
forero@edison06:/project/projectdirs/desi/users/forero/quicksurvey_example> date
Wed Nov 30 12:50:24 PST 2016
```

Total time: 
```bash
real	88m23.449s
user	134m48.073s
sys	8m41.153s
```
Ntargets:

```bash
source ELG target ELG truth ELG: selected 40458684 (40M) out of 79422779
source LRG target LRG truth LRG: selected 6087590 (6M) out of 11607022
source LYA target QSO truth QSO: selected 821018 (0.8M) out of 1526512
source QSO target QSO truth QSO: selected 2564940 (2.5M) out of 2695849
```

Notes:

`Multiprocess` keeps on running well after reading of QSOs finished.

### Bright

setup

```bash
forero@edison02:/project/projectdirs/desi/users/forero/quicksurvey_example> time ~/desitarget/bin/select_mock_targets -c input/mock_bright.yaml  -O input/bright/
forero@edison02:/project/projectdirs/desi/users/forero/quicksurvey_example> date
Wed Nov 30 12:52:12 PST 2016
```

Total time: 
```bash
real	95m40.995s
user	85m32.333s
sys	9m24.855s
```

Ntargets:

```bash
source BGS target BGS truth BGS: selected 19967171 (19M) out of 45136543
source MWS_MAIN target MWS_MAIN truth MWS_MAIN: selected 116347341 (116M) out of 318380785
source MWS_WD target MWS_WD truth MWS_WD: selected 742445 (0.7M) out of 930721
```

Notes:

MWS selection used a one magnitude brighter cut for the faint targets.

### Fake QSO

Ntargets:
```bash
source BADQSO target QSO truth STD_FSTAR: selected 80727977 (80M) out of 318380785
```
Notes:

The number of targets it's too large. The mismatch comes from the number density estimation which is done on a small 
patch and is not representative of the whole number density.

### Sky


total time
```bash
real	4m9.603s
user	3m51.918s
sys	0m22.477s
```

Ntargets
```bash
source SKY target SKY truth SKY: selected 23202610 (23M) out of 33128599
```

###standard stars

Ntargets
```bash
source STD_FSTAR target STD_FSTAR truth STD_FSTAR: selected 5661443 (5M) out of 201477132
```

Time
```bash
real	11m28.199s
user	6m45.713s
sys	3m35.773s
```

#All

```bash
No Fluctuations for this target SKY
mock area [ 16844.24500773] mock density [ 1966.76069392] - desired num density 1400.0
target_name STD_FSTAR : type: STD_FSTAR select: mag
Collects information across mock files
source BADQSO target QSO truth STD_FSTAR: selected 1804728 out of 318380785
source BGS target BGS truth BGS: selected 22387083 out of 45136543
source ELG target ELG truth ELG: selected 40471862 out of 79422779
source LRG target LRG truth LRG: selected 6092563 out of 11607022
source LYA target QSO truth QSO: selected 822990 out of 1526512
source MWS_MAIN target MWS_MAIN truth MWS_MAIN: selected 5046973 out of 318380785
source MWS_WD target MWS_WD truth MWS_WD: selected 742445 out of 930721
source QSO target QSO truth QSO: selected 2564894 out of 2695849
source SKY target SKY truth SKY: selected 23582478 out of 33128599
source STD_FSTAR target STD_FSTAR truth STD_FSTAR: selected 10626032 out of 318380785
Great total of 79933538 targets 10626032 stdstars 23582478 sky pos
Started writing StdStars file
Finished writing stdstars file
Started writing sky to file
Finished writing sky file
Started writing Targets file
WARNING: no real target catalog provided; adding columns of zeros for DECAM_FLUX, SHAPE*
Finished writing Targets file
Started computing the MTL file
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 37.28541016578674
DEBUG: calc_priority has 79933538 unobserved targets
0 of 79933538 targets have priority zero, setting N_obs=0.
Started writing the first MTL file
Finished writing mtl file
Started writing Truth file
Finished writing Truth file
done!

real	148m39.681s
user	171m35.327s
sys	12m24.475s


forero@edison02:/project/projectdirs/desi/users/forero/quicksurvey_example/input> ls -lh *.fits
-rw-rw---- 1 forero desi 8.2G Nov 30 18:38 mtl.fits
-rw-rw---- 1 forero desi 1.5G Nov 30 18:09 sky.fits
-rw-rw---- 1 forero desi 669M Nov 30 18:05 stdstars.fits
-rw-rw---- 1 forero desi 7.3G Nov 30 18:24 targets.fits
-rw-rw---- 1 forero desi 5.1G Nov 30 19:01 truth.fits
```
