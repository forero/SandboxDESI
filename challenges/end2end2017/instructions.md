### 0. Software

The following desihub products need to be installed.

* [desitarget](https://github.com/desihub/desitarget)
* [desisim](https://github.com/desihub/desisim)
* [fiberassign](https://github.com/desihub/fiberassign)

### 1. Mocks

Mocks for the Dark Time Survey have been generated using [CoLoRe](https://github.com/damonge/CoLoRe) (Cosmological Lognormal Realizations code by David Alonso). There are mockfiles stored in `$DESI_ROOT/mocks/GaussianRandomField/2048/`. 


### 2. Target and truth 

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


### 3. Standard Stars and Sky Positions

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


### 4. Epochs files

Epochs files list the IDs of the tiles that will be observed in a period of time before an updated version of the redshift catalog is available.

On NERSC here `/project/projectdirs/desi/users/forero/large_mock_test/input/epochs/` is a sample of 4 of such files. These re copies of the first four (out of 35) files prepared by Kyle Dawson here `/project/projectdirs/desi/datachallenge/Argonne2015/opsim2`.

### 5. Fiberassign template

`Fiberassign` takes a configuration file as an input. The python code running the simulation will update that file as needed based on a template. Here is an example of such file: `/project/projectdirs/desi/users/forero/large_mock_test/input/template/template_fiberassign.txt`.

### 6. Running quicksurvey

With all the sofware and files described in the previous software it is possible to run a the `quicksurvey` script in `desisim/bin`. It could be run as follows

```bash
./quicksurvey -O /project/projectdirs/desi/users/forero/large_mock_test/ -T /project/projectdirs/desi/users/forero/large_mock_test/input/files/ -f /global/homes/f/forero/fiberassign/bin/./fiberassign -E /project/projectdirs/desi/users/forero/large_mock_test/input/epochs/ -t /project/projectdirs/desi/users/forero/large_mock_test/input/template/template_fiberassign.txt -N 3
```
where 

* `/project/projectdirs/desi/users/forero/large_mock_test/` is the directory where all the outputs will be written.
* `/project/projectdirs/desi/users/forero/large_mock_test/files/` is the directory that hosts all the input `fits` files.
* `/project/projectdirs/desi/users/forero/large_mock_test/input/epochs/` is the directory with the `epochs*.dat` files.


This should produce the following kind of output

```bash
Epoch 0
690 tiles to be included in fiberassign
Fri Jul  8 06:38:26 2016 Starting MTL
Fri Jul  8 06:42:11 2016 Finished MTL
Fri Jul  8 06:42:11 2016 Launching fiberassign
Fri Jul  8 06:47:32 2016 Finished fiberassign
Fri Jul  8 06:47:32 2016 112 tiles to gather in zcat
Fri Jul  8 06:48:56 2016 Finished zcat
Epoch 1
578 tiles to be included in fiberassign
Fri Jul  8 06:49:08 2016 Starting MTL
```
