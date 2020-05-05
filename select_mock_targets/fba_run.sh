fba_run --targets bgs_targets/targets-bright.fits --sky targets/sky.fits --footprint footprint/tiles_bright.fits --rundate 2019-01-01T00:00:00 --dir fba_results/ --overwrite
fba_merge_results --targets bgs_targets/targets-bright.fits --sky targets/sky_south.fits  --dir fba_results/ 
fba_run_qa --dir fba_results/ --prefix fiberassign- --rundate 2019-01-01T00:00:00 

