#python ~/fiberassign/bin/fba_cmx --dr dr9 --dtver 0.49.0 --rundate 2021-02-22T00:00:00 --seed 77  --tilera 93.  --tiledec 57.3 --tileid 80843  --faflavor dithprec  --outdir ./20210224

mkdir -p $DESI_ROOT/users/forero/tiles_dither_20210224/
rm -v $DESI_ROOT/users/forero/tiles_dither_20210224/*
cp -v ./20210224/fiber* $DESI_ROOT/users/forero/tiles_dither_20210224/

#35.02  30.22  b=-29
# 99.0    66.00  b=+23
#110.36  78.76  b=+28
#23.4    1.00  b=+18