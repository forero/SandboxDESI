#!/bin/tcsh

# First clone the basic information for the instrument's model
svn --username jeforeroromero co https://desi.lbl.gov/svn/code/desimodel/trunk/ /gpfs/data/jeforero/desimodel

#setup the environment variable DESIMODEL
setenv DESIMODEL /gpfs/data/jeforero/desimodel/

