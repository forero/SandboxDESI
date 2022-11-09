

# On Perlmutter

(Main reference https://github.com/desihub/LSS/blob/main/Sandbox/LSSpipe_ab1stgen_Y1.txt)

1. Basic path setup

```
cd $PSCRATCH/MockLSS
source /global/common/software/desi/desi_environment.sh main
PYTHONPATH=$PYTHONPATH:$HOME/LSS/py
```


2. Prepare data to run fiberassign on the mocks 

```
salloc -N 1 -C cpu -t 04:00:00 --qos interactive --account desi
mkdir -p $PSCRATCH/MockLSS/FirstGenMocks/AbacusSummit//Y1/multipass_mock1_dark/

cd $HOME/LSS/scripts/mock_tools/
python $HOME/LSS/scripts/mock_tools/prepare_mocks_main.py --base_output $PSCRATCH/MockLSS/ --prep y --realmin 1 --realmax 2 --survey Y1 
```

3. Run fiberassign on the mocks (still in the intereactive session)

```
python $HOME/LSS/scripts/mock_tools/run_mocks_multipass.py --realmin 1 --realmax 2 --footprint Y1 --nproc 64 --base_output $PSCRATCH/MockLSS/ 
````


4. Prepare randoms (still within the previous session) and run fiberassign on them

```
python $HOME/LSS/scripts/mock_tools/prepare_mocks_ran_main.py --ranmin 1 --ranmax 2 --footprint Y1 --nproc 64 --base_output $PSCRATCH/MockLSS/
```



5. Combine across tiles for dark time info, default just does dark time. 
   Setting --add_gtl n means that we are not using the good fiber list from the actual observed data.

```
python $HOME/LSS/scripts/mock_tools/mkCat_mock.py  --mockmin 1 --mockmax 2 --survey Y1 --combd y --combr y --combdr y --tracer dark --add_gtl n --countran y --base_output $PSCRATCH/MockLSS/
```


6. Finally for each tracer (LRG, ELG, QSO)

```
python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer LRG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output $PSCRATCH/MockLSS/  --add_gtl n

python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer ELG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output $PSCRATCH/MockLSS/  --add_gtl n

python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer QSO --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output $PSCRATCH/MockLSS/  --add_gtl n
```


7. Compute correlation function data

```
cd $HOME/LSS/scripts/

source /global/common/software/desi/users/adematti/cosmodesi_environment.sh main

python xirunpc.py --basedir $PSCRATCH/MockLSS/FirstGenMocks/AbacusSummit/Y1/mock1/LSScats/ --tracer LRG --tracer LRG_complete --nran 1 --survey Y1 --outdir $PSCRATCH/MockLSS/FirstGenMocks/AbacusSummit/Y1/mock1/LSScats/corr/ --njack 10

python xirunpc.py --basedir $PSCRATCH/MockLSS/FirstGenMocks/AbacusSummit/Y1/mock1/LSScats/ --tracer ELG --tracer ELG_complete --nran 1 --survey Y1 --outdir $PSCRATCH/MockLSS/FirstGenMocks/AbacusSummit/Y1/mock1/LSScats/corr/ --njack 10

python xirunpc.py --basedir $PSCRATCH/MockLSS/FirstGenMocks/AbacusSummit/Y1/mock1/LSScats/ --tracer QSO --tracer QSO_complete --nran 1 --survey Y1 --outdir $PSCRATCH/MockLSS/FirstGenMocks/AbacusSummit/Y1/mock1/LSScats/corr/ --njack 10
```
