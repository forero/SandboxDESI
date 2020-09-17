import tiles as t

t.split_tiles(output_path="./tiles")

t.tiles_into_passes(input_tiles="tiles_cut_A_dark_north.fits", input_path="tiles", output_path="tiles")