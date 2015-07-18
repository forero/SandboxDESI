* Clone the basic information for the tiling and focal plane 
```
svn --username jeforeroromero co https://desi.lbl.gov/svn/code/desimodel/trunk/ /gpfs/data/jeforero/desimodel
```

* Setup the environment variable DESIMODEL

```
setenv DESIMODEL /gpfs/data/jeforero/desimodel/
```

* Clone the repository to manipulate mocks and make target selection
```
git clone https://github.com/desihub/desitarget.git /gpfs/data/jeforero/desitarget/
```

* Check and run the example to read a lightcone and make the target selection 
```
cd /gpfs/data/jeforero/desitarget/py/desitarget
cat example.py # the function cut_example()
```

* Check and run the example to translate the FITS file into binary format
```
cd /gpfs/data/jeforero/desitarget/py/desitarget
cat example.py # the function fits_to_bin_example()
```

* Clone the repository for fiberassign (Bob Cahn's)

```
git clone https://github.com/desihub/fiberassign.git /gpfs/data/jeforero/fiberassign/
```

* Go to the fiberassign directory, compile in src/ with Makefile.cosma
```
cd /gpfs/data/jeforero/fiberassign/src
make -f Makefile.cosma
```

* Go to the fiberassign directory, and verify the setup file and the submission script

```
cd /gpfs/data/jeforero/fiberassign/script
cat feature_cosma.txt
cat run_cosma.job
```
