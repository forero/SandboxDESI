fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-03-17T23:20:01 --seed 77  --tilera 160.0  --tiledec 50.0 --tileid 80903  --faflavor dithprec  --outdir tiles_dither_march
fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-03-17T23:20:01 --seed 77  --tilera 160.0  --tiledec 50.0 --tileid 80916  --faflavor dithfocus  --outdir tiles_dither_march
rm -v $DESI_ROOT/users/forero/tiles_dither_march/*
cp -v ./tiles_dither_march/fiber* $DESI_ROOT/users/forero/tiles_dither_march/
