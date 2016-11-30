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

