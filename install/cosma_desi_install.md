* Clone the basic information for the instrument's model 
```
svn --username jeforeroromero co https://desi.lbl.gov/svn/code/desimodel/trunk/ /gpfs/data/jeforero/desimodel
```

* Setup the environment variable DESIMODEL

```
setenv DESIMODEL /gpfs/data/jeforero/desimodel/
```

* Clone the repository for FiberAsssign (Bob Cahn's)

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
