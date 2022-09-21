# On Perlmutter

1. Basic path setup
```
cd $PSCRATCH/MockLSS
source /global/common/software/desi/desi_environment.sh main
PYTHONPATH=$PYTHONPATH:$HOME/LSS/py
```

2. Prepare data to run fiberassign on the mocks
```
salloc -N 1 -C cpu -t 04:00:00 --qos interactive --account desi
python $HOME/LSS/scripts/mock_tools/run_mocks_multipass.py --realmin 1 --realmax 2 --footprint Y1 --nproc 64 --base_output $PSCRATCH/MockLSS --prep y
```
