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

3. Now this could be done outside the interactive session

```
python $HOME/LSS/scripts/mock_tools/mkCat_mock.py  --mockmin 1 --mockmax 2 --survey Y1 --combd y --combr y --combdr y --tracer dark --add_gtl n --countran y --base_output /global/cscratch1/sd/forero/tmp/ 
```

4. Finally for each tracer (LRG, ELG, QSO)

```
python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer LRG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output /global/cscratch1/sd/forero/tmp/  --add_gtl n

python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer ELG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output /global/cscratch1/sd/forero/tmp/  --add_gtl n

python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer QSO --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output /global/cscratch1/sd/forero/tmp/  --add_gtl n
```
