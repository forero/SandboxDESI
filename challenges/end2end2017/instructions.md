### 1. Mocks

Mocks for the Dark Time Survey have been generated using [CoLoRe](https://github.com/damonge/CoLoRe) (Cosmological Lognormal Realizations code by David Alonso). There are mockfiles stored in `$DESI_ROOT/mocks/GaussianRandomField/2048/`. 


### 2. Target and truth files

Targets and truth can be generated from the Mocks using the `mock_targets_darktime` script in `desitargets/bin`.

```bash
./mock_targets_darktime  -Q $DESI_ROOT/mocks/GaussianRandomField/2048/QSO.fits -L $DESI_ROOT/project/projectdirs/desi/mocks/GaussianRandomField/2048/LRG.fits -E $DESI_ROOT/project/projectdirs/desi/mocks/GaussianRandomField/2048/LRG.fits  -C /project/projectdirs/desi/mocks/GaussianRandomField/2048/QSO.fits

```
