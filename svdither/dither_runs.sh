python ~/fiberassign/bin/fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-01-20T00:00:00 --seed 77  --tilera 188.0  --tiledec 30.0 --tileid 80743  --faflavor dithprec  --outdir ./080743
python ~/fiberassign/bin/fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-01-20T00:00:00 --seed 77  --tilera 111.64  --tiledec 30.0 --tileid 80756  --faflavor dithprec  --outdir ./080756
python ~/fiberassign/bin/fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-01-20T00:00:00 --seed 77  --tilera 111.64  --tiledec 30.0 --tileid 80769  --faflavor dithfocus --outdir ./080769
rm -v $DESI_ROOT/users/forero/tiles_dither_february/*
cp -v ./080*/fiber* $DESI_ROOT/users/forero/tiles_dither_february/