1. Setup DESIMODEL
==================

* Clone the basic information for the tiling and focal plane 
```
svn --username jeforeroromero co https://desi.lbl.gov/svn/code/desimodel/trunk/ /gpfs/data/jeforero/desimodel
```

* Setup the environment variable DESIMODEL

```
setenv DESIMODEL /gpfs/data/jeforero/desimodel/
```

2. Make TARGET SELECTION
========================

* Clone the repository to manipulate mocks and make target selection
```
git clone https://github.com/desihub/desitarget.git /gpfs/data/jeforero/desitarget/
```

* Check and run the example to read a lightcone and make the target selection. At this point you have to edit example.py and uncomment the line with the function ```cut_example()```

```
cd /gpfs/data/jeforero/desitarget/py/desitarget
cat example.py # the function cut_example()
```



* Check and run the example to translate the FITS file into binary format. At this point you have to edit example.py and uncomment the line with the function ```fits_to_bin_example()```
```
cd /gpfs/data/jeforero/desitarget/py/desitarget
cat example.py # the function fits_to_bin_example()
```

3. Run FIBERASSIGN
========================

* Clone the repository for fiberassign (Bob Cahn's) and move into the directory

```
git clone https://github.com/desihub/fiberassign.git /gpfs/data/jeforero/fiberassign/
cd /gpfs/data/jeforero/fiberassign/
```


* Change to the stable branch

```
git checkout Vtalk0
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
