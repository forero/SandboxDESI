

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
----

5. Finally for each tracer (LRG, ELG, QSO)

```
python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer LRG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output $PSCRATCH/MockLSS/  --add_gtl n

python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer ELG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output $PSCRATCH/MockLSS/  --add_gtl n

python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer QSO --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot y --mkclusdat_allpot y --nz y --base_output $PSCRATCH/MockLSS/  --add_gtl n
```

LRG fails with

```
Traceback (most recent call last):
  File "/global/homes/f/forero/LSS/scripts/mock_tools/mkCat_mock.py", line 435, in <module>
    docat(mn,i)
  File "/global/homes/f/forero/LSS/scripts/mock_tools/mkCat_mock.py", line 336, in docat
    ztab = Table(fitsio.read(tarf,columns=['TARGETID','RSDZ']))
  File "/global/common/software/desi/perlmutter/desiconda/20220119-2.0.1/conda/lib/python3.9/site-packages/fitsio/fitslib.py", line 139, in read
    with FITS(filename, **kwargs) as fits:
  File "/global/common/software/desi/perlmutter/desiconda/20220119-2.0.1/conda/lib/python3.9/site-packages/fitsio/fitslib.py", line 520, in __init__
    self._FITS = _fitsio_wrap.FITS(filename, self.intmode, create)
OSError: FITSIO status = 104: could not open the named file
failed to find or open the following file: (ffopen)
/pscratch/sd/f/forero/MockLSS/FirstGenMocks/AbacusSummit/Y1/fba1/targs.fits
```
So, instead use `n` in `mkclustdat_allpot` and `mkclusran_allpot`.

```
python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer LRG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot n --mkclusdat_allpot n --nz y --base_output $PSCRATCH/MockLSS/  --add_gtl n

python $HOME/LSS/scripts/mock_tools/mkCat_mock.py --tracer ELG --mockmin 1 --mockmax 2 --survey Y1 --fulld y --fullr y --apply_veto y --mkclusran y --mkclusdat y --mkclusran_allpot n --mkclusdat_allpot n --nz y --base_output $PSCRATCH/MockLSS/  --add_gtl n
```


6. Make plots

```
cd $HOME/LSS/scripts/
python xirunpc.py --basedir argument ($desi/survey/catalogs/main/mocks/FirstGenMocks/AbacusSummit/Y1/mock1/LSScats/ --tracer LRG --tracer LRG_complete
```
