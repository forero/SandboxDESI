### 0. Software

The following desihub products need to be installed.

* [desitarget](https://github.com/desihub/desitarget)
* [desisim](https://github.com/desihub/desisim)
* [fiberassign](https://github.com/desihub/fiberassign)
* [desisurvey](https://github.com/desihub/desisurvey)
* [surveysim](https://github.com/desihub/surveysim)

Tutorials on [Getting started at NERSC](https://desi.lbl.gov/trac/wiki/Pipeline/GettingStarted/NERSC) and [Installing DESI code on your laptop or other machine](https://desi.lbl.gov/trac/wiki/Pipeline/GettingStarted/Laptop/JuneMeeting).  

### 1. Survey Strategy

Follow the instructions in [this tutorial](https://github.com/desihub/surveysim/blob/master/doc/tutorial.md) to 
generate a sequence of tile exposures together with its weather conditions.

========

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

On NERSC here `/project/projectdirs/desi/users/forero/datachallenge2017/test/input/epochs/` is a sample of 8 of such files. Those correspond to a small patch in RA,DEC (~400 deg^2) matching the input mock files in `/project/projectdirs/desi/users/forero/datachallenge2017/test/input/`.

### 4. Fiberassign template

`Fiberassign` takes a configuration file as an input. The python code running the simulation will update that file as needed based on a template. Here is an example of such file: `/project/projectdirs/desi/users/forero/datachallenge2017/test/input/template/template_fiberassign.txt`.

### 5. Running quicksurvey

With all the sofware and files described in the previous software it is possible to run a the `quicksurvey` script in `desisim/bin`. It could be run as follows

```bash
./quicksurvey -O /project/projectdirs/desi/users/forero/datachallenge2017/test/ -T /project/projectdirs/desi/users/forero/datachallenge2017/test/input/ -f ~/fiberassign/bin/./fiberassign -E /project/projectdirs/desi/users/forero/datachallenge2017/test/input/epochs/ -t /project/projectdirs/desi/users/forero/datachallenge2017/test/input/template/template_fiberassign.txt -N 8
```
where 

* `-O /project/projectdirs/desi/users/forero/datachallenge2017/test/` indicates the directory where all the outputs will be written.
* `-T /project/projectdirs/desi/users/forero/datachallenge2017/test/input/` indicates the directory that hosts all the input `fits` files.
* `-E /project/projectdirs/desi/users/forero/datachallenge2017/test/input/epochs/` indicates the directory with the `epochs*.dat` files.


This should produce the following kind of output

```bash
Epoch 0
462 tiles to be included in fiberassign
Tue Nov  8 17:32:54 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.5092618465423584
DEBUG: calc_priority has 2330308 unobserved targets
0 of 2330308 targets have priority zero, setting N_obs=0.
Tue Nov  8 17:33:10 2016 Finished MTL
Tue Nov  8 17:33:10 2016 Launching fiberassign
Tue Nov  8 17:34:57 2016 Finished fiberassign
Tue Nov  8 17:34:57 2016 58 tiles to gather in zcat
Tue Nov  8 17:35:08 2016 Finished zcat
Epoch 1
404 tiles to be included in fiberassign
Tue Nov  8 17:35:08 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.5397968292236328
DEBUG: calc_priority has 2103062 unobserved targets
157326 of 2330308 targets have priority zero, setting N_obs=0.
/global/common/edison/contrib/desi/conda/conda_3.5-20160829/lib/python3.5/site-packages/astropy/table/column.py:1095: MaskedArrayFutureWarning: setting an item on a masked array which has a shared mask will not copy the mask and also change the original mask array in the future.
Check the NumPy 1.11 release notes for more information.
  ma.MaskedArray.__setitem__(self, index, value)
Tue Nov  8 17:36:17 2016 Finished MTL
Tue Nov  8 17:36:18 2016 Launching fiberassign
Tue Nov  8 17:37:51 2016 Finished fiberassign
Tue Nov  8 17:37:51 2016 57 tiles to gather in zcat
Tue Nov  8 17:38:11 2016 Finished zcat
Epoch 2
347 tiles to be included in fiberassign
Tue Nov  8 17:38:11 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.7001972198486328
DEBUG: calc_priority has 1911750 unobserved targets
348624 of 2330308 targets have priority zero, setting N_obs=0.
Tue Nov  8 17:38:56 2016 Finished MTL
Tue Nov  8 17:38:56 2016 Launching fiberassign
Tue Nov  8 17:41:05 2016 Finished fiberassign
Tue Nov  8 17:41:05 2016 57 tiles to gather in zcat
Tue Nov  8 17:41:33 2016 Finished zcat
Epoch 3
290 tiles to be included in fiberassign
Tue Nov  8 17:41:33 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.6633102893829346
DEBUG: calc_priority has 1716476 unobserved targets
554130 of 2330308 targets have priority zero, setting N_obs=0.
Tue Nov  8 17:42:19 2016 Finished MTL
Tue Nov  8 17:42:19 2016 Launching fiberassign
Tue Nov  8 17:43:38 2016 Finished fiberassign
Tue Nov  8 17:43:38 2016 59 tiles to gather in zcat
Tue Nov  8 17:44:15 2016 Finished zcat
Epoch 4
231 tiles to be included in fiberassign
Tue Nov  8 17:44:15 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.6961843967437744
DEBUG: calc_priority has 1507803 unobserved targets
761648 of 2330308 targets have priority zero, setting N_obs=0.
Tue Nov  8 17:44:58 2016 Finished MTL
Tue Nov  8 17:44:58 2016 Launching fiberassign
Tue Nov  8 17:46:28 2016 Finished fiberassign
Tue Nov  8 17:46:28 2016 59 tiles to gather in zcat
Tue Nov  8 17:47:13 2016 Finished zcat
Epoch 5
172 tiles to be included in fiberassign
Tue Nov  8 17:47:13 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.46558690071105957
DEBUG: calc_priority has 1290415 unobserved targets
960433 of 2330308 targets have priority zero, setting N_obs=0.
Tue Nov  8 17:47:55 2016 Finished MTL
Tue Nov  8 17:47:55 2016 Launching fiberassign
Tue Nov  8 17:48:33 2016 Finished fiberassign
Tue Nov  8 17:48:33 2016 58 tiles to gather in zcat
Tue Nov  8 17:49:25 2016 Finished zcat
Epoch 6
114 tiles to be included in fiberassign
Tue Nov  8 17:49:25 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.5565974712371826
DEBUG: calc_priority has 1086320 unobserved targets
1157320 of 2330308 targets have priority zero, setting N_obs=0.
Tue Nov  8 17:50:05 2016 Finished MTL
Tue Nov  8 17:50:05 2016 Launching fiberassign
Tue Nov  8 17:50:38 2016 Finished fiberassign
Tue Nov  8 17:50:38 2016 57 tiles to gather in zcat
Tue Nov  8 17:51:37 2016 Finished zcat
Epoch 7
57 tiles to be included in fiberassign
Tue Nov  8 17:51:38 2016 Starting MTL
DEBUG: before targets.calc_priority slow copy
DEBUG: seconds for targets.calc_priority slow copy: 0.433809757232666
DEBUG: calc_priority has 891698 unobserved targets
1351291 of 2330308 targets have priority zero, setting N_obs=0.
Tue Nov  8 17:52:19 2016 Finished MTL
Tue Nov  8 17:52:19 2016 Launching fiberassign
Tue Nov  8 17:52:40 2016 Finished fiberassign
Tue Nov  8 17:52:41 2016 57 tiles to gather in zcat
Tue Nov  8 17:53:50 2016 Finished zcat
```
