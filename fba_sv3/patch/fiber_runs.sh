# Bright with secondaries
fba_run --targets inputs/mtl_bright_sv3_onepct.fits  --sky inputs/sky_onepct.fits --footprint inputs/one_pct_bright_tiles.fits --rundate 2021-03-17T23:20:01 --dir fba_mtl_bright_sv3_onepct/ --overwrite --no_redistribute &

# updated BGS without secondaries
#fba_run --targets inputs/mtl_updated_bgs_bright_sv3_onepct.fits  --sky inputs/sky_onepct.fits --footprint inputs/one_pct_bright_tiles.fits --rundate 2021-03-17T23:20:01 --dir fba_mtl_updated_bgs_bright_sv3_onepct/ --overwrite &

# updated BGS with secondaries
#fba_run --targets inputs/mtl_updated_bgs_bright_sv3_onepct.fits inputs/secondary_bright_sv3_onepct.fits --sky inputs/sky_onepct.fits --footprint inputs/one_pct_bright_tiles.fits --rundate 2021-03-17T23:20:01 --dir fba_scnd_mtl_updated_bgs_bright_sv3_onepct/ --overwrite &

# DARK without secondaries
fba_run --targets inputs/mtl_updated_lya_0.20_dark_sv3_onepct.fits --sky inputs/sky_onepct.fits --footprint inputs/one_pct_dark_tiles.fits --rundate 2021-03-17T23:20:01 --dir fba_mtl_updated_lya_0.20_dark_sv3_onepct/ --overwrite  --no_redistribute  &
