fba_run --targets targets/dark_south.fits --sky targets/sky_south.fits  --footprint footprint/tiles_dark_south.fits --rundate 2019-01-01T00:00:00 --dir fba_dark_south/ --overwrite 
fba_run --targets targets/dark_north.fits --sky targets/sky_north.fits  --footprint footprint/tiles_dark_north.fits --rundate 2019-01-01T00:00:00 --dir fba_dark_north/ --overwrite 
fba_run --targets targets/bright_south.fits --sky targets/sky_south.fits --footprint footprint/tiles_bright_south.fits --rundate 2019-01-01T00:00:00 --dir fba_bright_south/ --overwrite
fba_run --targets targets/bright_north.fits --sky targets/sky_north.fits --footprint footprint/tiles_bright_north.fits --rundate 2019-01-01T00:00:00 --dir fba_bright_north/ --overwrite


fba_merge_results --targets targets/dark_south.fits --sky targets/sky_south.fits  --dir fba_dark_south/ 
fba_merge_results --targets targets/dark_north.fits --sky targets/sky_north.fits --dir fba_dark_north/
fba_merge_results --targets targets/bright_south.fits --sky targets/sky_south.fits --dir fba_bright_south/
fba_merge_results --targets targets/bright_north.fits --sky targets/sky_north.fits --dir fba_bright_north/

fba_run_qa --dir fba_dark_south/ --prefix fiberassign- --rundate 2019-01-01T00:00:00 
fba_run_qa --dir fba_dark_north/ --prefix fiberassign- --rundate 2019-01-01T00:00:00 
fba_run_qa --dir fba_bright_south/ --prefix fiberassign- --rundate 2019-01-01T00:00:00 
fba_run_qa --dir fba_bright_north/ --prefix fiberassign- --rundate 2019-01-01T00:00:00 

