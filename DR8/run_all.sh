#fba_run --targets targets/dark_gray_south.fits --sky targets/sky_south.fits  --footprint footprint/tiles_dark_gray_south.fits --rundate 2019-01-01T00:00:00 --dir fba_dark_gray_south/ --overwrite 
#fba_run --targets targets/dark_gray_north.fits --sky targets/sky_north.fits  --footprint footprint/tiles_dark_gray_north.fits --rundate 2019-01-01T00:00:00 --dir fba_dark_gray_north/ --overwrite 
#fba_run --targets targets/bright_south.fits --sky targets/sky_south.fits --footprint footprint/tiles_bright_south.fits --rundate 2019-01-01T00:00:00 --dir fba_bright_south/ --overwrite
#fba_run --targets targets/bright_north.fits --sky targets/sky_north.fits --footprint footprint/tiles_bright_north.fits --rundate 2019-01-01T00:00:00 --dir fba_bright_north/ --overwrite


fba_merge_results --targets targets/dark_gray_south.fits --sky targets/sky_south.fits  --dir fba_dark_gray_south/ 
fba_merge_results --targets targets/dark_gray_north.fits --sky targets/sky_north.fits --dir fba_dark_gray_north/
fba_merge_results --targets targets/bright_south.fits --sky targets/sky_south.fits --dir fba_bright_south/
fba_merge_results --targets targets/bright_north.fits --sky targets/sky_north.fits --dir fba_bright_north/

