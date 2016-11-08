### 0. Software

The following desihub products need to be installed.

* [desitarget](https://github.com/desihub/desitarget)
* [desisim](https://github.com/desihub/desisim)
* [fiberassign](https://github.com/desihub/fiberassign)

### 1. Mocks

There are different kinds of mocks. All of them can be found in
`$DESI_ROOT/mocks/`.  


### 2. Target, Truth, Starndard Stars and Sky Positions

These files can be generated using a single script in `desitarget/bin`.

```bash
./select_mock_targets --config input.yaml
```
Where the `input.yaml` file can be found in `desitarget/doc/mock_example`

### 3. Epochs files

Epochs files list the IDs of the tiles that will be observed in a period of time before an updated version of the redshift catalog is available.

On NERSC here `/project/projectdirs/desi/users/forero/large_mock_test/input/epochs/` is a sample of 4 of such files. These re copies of the first four (out of 35) files prepared by Kyle Dawson here `/project/projectdirs/desi/datachallenge/Argonne2015/opsim2`.

### 4. Fiberassign template

`Fiberassign` takes a configuration file as an input. The python code running the simulation will update that file as needed based on a template. Here is an example of such file: `/project/projectdirs/desi/users/forero/large_mock_test/input/template/template_fiberassign.txt`.

### 5. Running quicksurvey

With all the sofware and files described in the previous software it is possible to run a the `quicksurvey` script in `desisim/bin`. It could be run as follows

```bash
./quicksurvey -O /project/projectdirs/desi/users/forero/datachallenge2017/test/ -T /project/projectdirs/desi/users/forero/datachallenge2017/test/input/ -f ~/fiberassign/bin/./fiberassign -E /project/projectdirs/desi/users/forero/datachallenge2017/test/input/epochs/ -t /project/projectdirs/desi/users/forero/datachallenge2017/test/input/template/template_fiberassign.txt -N 8
```
where 

* `-O /project/projectdirs/desi/users/forero/large_mock_test/` indicates the directory where all the outputs will be written.
* `-T /project/projectdirs/desi/users/forero/large_mock_test/files/` indicates the directory that hosts all the input `fits` files.
* `-E /project/projectdirs/desi/users/forero/large_mock_test/input/epochs/` indicates the directory with the `epochs*.dat` files.


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
Fri Jul  8 07:01:19 2016 Finished MTL
Fri Jul  8 07:01:20 2016 Launching fiberassign
Fri Jul  8 07:07:22 2016 Finished fiberassign
Fri Jul  8 07:07:22 2016 382 tiles to gather in zcat
Fri Jul  8 07:10:03 2016 Finished zcat
Epoch 2
196 tiles to be included in fiberassign
Fri Jul  8 07:10:15 2016 Starting MTL
Fri Jul  8 07:19:22 2016 Finished MTL
Fri Jul  8 07:19:22 2016 Launching fiberassign
Fri Jul  8 07:22:23 2016 Finished fiberassign
Fri Jul  8 07:22:23 2016 196 tiles to gather in zcat
Fri Jul  8 07:24:34 2016 Finished zcat
```
