import DR8 as dr8


limits_cut = {'min_ra':175, 'max_ra':180, 'min_dec':-2.5, 'max_dec':2.5, 'name':'cut_E'}
dr8.cut_mtl_sky_tiles(targets_path="./targets/", tile_path="./tiles/", 
                      cut_name = limits_cut['name'], limits=limits_cut)

limits_cut = {'min_ra':170, 'max_ra':190, 'min_dec':-5, 'max_dec':5, 'name':'cut_D'}
dr8.cut_mtl_sky_tiles(targets_path="./targets/", tile_path="./tiles/", 
                      cut_name = limits_cut['name'], limits=limits_cut)

limits_cut = {'min_ra':160, 'max_ra':200, 'min_dec':-10, 'max_dec':10, 'name':'cut_C'}
dr8.cut_mtl_sky_tiles(targets_path="./targets/", tile_path="./tiles/", 
                      cut_name = limits_cut['name'], limits=limits_cut)

limits_cut = {'min_ra':0, 'max_ra':360, 'min_dec':-10, 'max_dec':30, 'name':'cut_B'}
dr8.cut_mtl_sky_tiles(targets_path="./targets/", tile_path="./tiles/", 
                      cut_name = limits_cut['name'], limits=limits_cut)

limits_cut = {'min_ra':0, 'max_ra':360, 'min_dec':-90, 'max_dec':90, 'name':'cut_A'}
dr8.cut_mtl_sky_tiles(targets_path="./targets/", tile_path="./tiles/", 
                      cut_name = limits_cut['name'], limits=limits_cut)