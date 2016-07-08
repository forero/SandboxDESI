### 1. Mocks

Mocks for the Dark Time Survey have been generated using [CoLoRe](https://github.com/damonge/CoLoRe) (Cosmological Lognormal Realizations code by David Alonso). There are mockfiles stored in `$DESI_ROOT/mocks/GaussianRandomField/2048/`. 


### 2. Target and truth files

Targets and truth can be generated from the Mocks using the `mock_targets_darktime` script in `desitarget/bin`.

```bash
./mock_targets_darktime  -Q $DESI_ROOT/mocks/GaussianRandomField/2048/QSO.fits -L $DESI_ROOT/mocks/GaussianRandomField/2048/LRG.fits -E $DESI_ROOT/mocks/GaussianRandomField/2048/ELG.fits  -C $DESI_ROOT/mocks/GaussianRandomField/2048/random.fits
```

This should produce the following kind of output

```bash
WARNING: mock cannot achieve the goal density for true_type QSO. Goal 120.0. Mock 1e-06
WARNING: mock cannot achieve the goal density for true_type GALAXY. Goal 2400.0. Mock 2391.9311211
Total in targetid 48575429
```

The first `WARNING` is there because at the moment Lya QSOs with redshift z>2.1 have not been included in the mocks. 
The second `WARNING` indicates that the number density in the mock is slightly below the goal number density.
There must be now two new files `targets.fits` and `truth.fits` in the working directory.


### 3. Standard Stars and Sky Positions.

Standard Stars and Sky Positions can be generated from the random mocks using the `mock_skypos_stdstars_darktime` script in `desitarget/bin` .

```bash
./mock_skypos_stdstars_darktime -R $DESI_ROOT/mocks/GaussianRandomField/2048/random.fits
```

This should produce the following kind of output.

```bash
Total in targetid 2321266
Total in targetid 23206875
```

There must be now two new files `stdstars.fits` and `sky.fits` in the working directory.
