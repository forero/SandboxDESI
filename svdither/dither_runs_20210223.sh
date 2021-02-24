python ~/fiberassign/bin/fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-02-22T00:00:00 --seed 77  --tilera 35.02  --tiledec 30.22 --tileid 80791  --faflavor dithprec  --outdir ./20210223
python ~/fiberassign/bin/fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-02-22T00:00:00 --seed 77  --tilera 99.0  --tiledec 66.0 --tileid 80804  --faflavor dithprec  --outdir ./20210223
python ~/fiberassign/bin/fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-02-22T00:00:00 --seed 77  --tilera 110.36  --tiledec 78.76 --tileid 80817  --faflavor dithprec --outdir ./20210223
python ~/fiberassign/bin/fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-02-22T00:00:00 --seed 77  --tilera 123.4  --tiledec 1.0 --tileid 80830  --faflavor dithprec --outdir ./20210223

mkdir -p $DESI_ROOT/users/forero/tiles_dither_20210223/*
rm -v $DESI_ROOT/users/forero/tiles_dither_20210223/*
cp -v ./20210223/fiber* $DESI_ROOT/users/forero/tiles_dither_20210223/

#35.02  30.22  b=-29
# 99.0    66.00  b=+23
#110.36  78.76  b=+28
#23.4    1.00  b=+18