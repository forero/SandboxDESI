

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
python $HOME/LSS/scripts/mock_tools/run_mocks_multipass.py --realmin 1 --realmax 2 --footprint Y1 --nproc 64 --base_output $PSCRATCH/MockLSS/ --prep y
```

----

3. Prepare randoms (still within the previous session)

```
python $HOME/LSS/scripts/mock_tools/prepare_mocks_ran_main.py --ranmin 1 --ranmax 2 --footprint Y1 --nproc 64 --base_output $PSCRATCH/MockLSS/
```



4. Combine across tiles for dark time info, default just does dark time. 
   Setting --add_gtl n means that we are not using the good fiber list from the actual observed data.

```
python $HOME/LSS/scripts/mock_tools/mkCat_mock.py  --mockmin 1 --mockmax 2 --survey Y1 --combd y --combr y --combdr y --tracer dark --add_gtl n --countran y --base_output $PSCRATCH/MockLSS/
```

5. Finally for each tracer (LRG, ELG, QSO)

```
python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer LRG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output $PSCRATCH/MockLSS  --add_gtl n

python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer ELG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output $PSCRATCH/MockLSS  --add_gtl n

python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer QSO --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output $PSCRATCH/MockLSS  --add_gtl n
```

6. Make plots

```
cd $HOME/LSS/scripts/
python xirunpc.py --basedir argument ($desi/survey/catalogs/main/mocks/FirstGenMocks/AbacusSummit/Y1/mock1/LSScats/ --tracer LRG --tracer LRG_complete
```


# On Cori, Y1

1. Basic path setup

```
cd $SCRATCH/MockLSS
source /global/common/software/desi/desi_environment.sh main
PYTHONPATH=$PYTHONPATH:$HOME/LSS/py
```


2. Prepare data to run fiberassign on the mocks

```
salloc -N 1 -C cpu -t 04:00:00 --qos interactive -C haswell
mkdir -p $SCRATCH/MockLSS/FirstGenMocks/AbacusSummit/Y1/multipass_mock1_dark/
cd $HOME/LSS/scripts/mock_tools/
python $HOME/LSS/scripts/mock_tools/run_mocks_multipass.py --realmin 1 --realmax 2 --footprint Y1 --nproc 32 --base_output $SCRATCH/MockLSS --prep y
```

3. Prepare randoms (in a new large memory session)

```
module load cmem
cd $HOME/LSS/scripts/mock_tools/
salloc -N 1 -C amd -t 4:00:00 -q interactive
python $HOME/LSS/scripts/mock_tools/prepare_mocks_ran_main.py --ranmin 1 --ranmax 2 --footprint Y1 --nproc 32
```
