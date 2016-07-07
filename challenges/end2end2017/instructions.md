### Mocks

Mocks have been generated using [CoLoRe](https://github.com/damonge/CoLoRe) (Cosmological Lognormal Realizations code by David Alonso).

There are mockfiles stored in `$DESI_ROOT/mocks/GaussianRandomField/2048/`. 
Each file is a FITS table with the following columns:

ra : right ascension angle [degrees]
dec : declination angle [degrees]
z : comoving distance converted to redshift using LCDM
dz : redshift space distortion calculated from linear velocity field

### Target and truth files

Targets and truth can be generated using the `mock_targets_darktime` script in `desitargets/bin`.