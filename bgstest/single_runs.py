import glob

tiles = glob.glob("tiles/tile_*_dark.fits")
tiles.sort()

for tile in tiles:
    cmd = "time fba_run --targets targets/mtl_dark_onepct.fits --sky targets/sky_onepct.fits --footprint {} --rundate 2020-01-01T00:00:00 --dir fba_output_single_dark/ --overwrite; ".format(tile)
    cmd = "{ " + cmd + " }  2>> timings.txt"
    print(cmd)