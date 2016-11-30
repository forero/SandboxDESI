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

#Bright

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
