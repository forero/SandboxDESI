fba_run --targets inputs/mtl_bright_sv3_onepct.fits  --sky inputs/sky_onepct.fits --footprint inputs/one_pct_bright_tiles.fits --rundate 2021-04-20T10:00:00 --dir fba_mtl_bright_sv3_onepct/ --overwrite --no_redistribute &

fba_run --targets inputs/mtl_updated_lya_0.20_dark_sv3_onepct.fits --sky inputs/sky_onepct.fits --footprint inputs/one_pct_dark_tiles.fits --rundate 2021-04-20T10:00:00 --dir fba_mtl_updated_lya_0.20_dark_sv3_onepct/ --overwrite  --no_redistribute  &
