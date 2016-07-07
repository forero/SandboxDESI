### 1. Mocks

Mocks for the Dark Time Survey have been generated using [CoLoRe](https://github.com/damonge/CoLoRe) (Cosmological Lognormal Realizations code by David Alonso). There are mockfiles stored in `$DESI_ROOT/mocks/GaussianRandomField/2048/`. 


### 2. Target and truth files

Targets and truth can be generated from the Mocks using the `mock_targets_darktime` script in `desitargets/bin`.

```bash
/mock_targets_darktime  -Q $DESI_ROOT/mocks/GaussianRandomField/2048/QSO.fits -L $DESI_ROOT/mocks/GaussianRandomField/2048/LRG.fits -E $DESI_ROOT/mocks/GaussianRandomField/2048/LRG.fits  -C $DESI_ROOT/mocks/GaussianRandomField/2048/QSO.fits
```

This should produce the following kind of output

```bash
WARNING: mock cannot achieve the goal density for true_type QSO. Goal 120.0. Mock 1e-06
Total in targetid 7273552
```

The `WARNING` is there because at the moment Lya QSOs with redshift z>2.1 have not been included in the mocks. 
