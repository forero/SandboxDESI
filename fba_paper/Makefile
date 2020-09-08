all: all_tiles all_targets all_cuts all_fba

all_tiles: 
	python prepare_tiles.py

all_targets: 
	python prepare_DR8_targets.py
    
all_cuts: 
	python prepare_cuts.py

all_fba:
	fba_run --targets targets/mtl_cut_D_dark_north.fits --sky targets/sky_cut_D_north.fits --footprint tiles/tiles_cut_D_dark_north.fits --rundate 2020-01-01T00:00:00 --dir fba_run/mtl_cut_D_tiles_cut_D/