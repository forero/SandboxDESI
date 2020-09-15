import join as j

j.join_fba_targets(targets_file="targets/mtl_cut_E_dark_north.fits", 
                 fba_path="fba_run/mtl_cut_E_tiles_cut_E/", 
                 summary_filename="summary/fba_summary_mtl_cut_E_tiles_cut_E.fits")

j.join_fba_targets(targets_file="targets/mtl_cut_D_dark_north.fits", 
                 fba_path="fba_run/mtl_cut_D_tiles_cut_D/", 
                 summary_filename="summary/fba_summary_mtl_cut_D_tiles_cut_D.fits")

j.join_fba_targets(targets_file="targets/mtl_cut_C_dark_north.fits", 
                 fba_path="fba_run/mtl_cut_C_tiles_cut_C/", 
                 summary_filename="summary/fba_summary_mtl_cut_C_tiles_cut_C.fits")

j.join_fba_targets(targets_file="targets/mtl_cut_B_dark_north.fits", 
                 fba_path="fba_run/mtl_cut_B_tiles_cut_B/", 
                 summary_filename="summary/fba_summary_mtl_cut_B_tiles_cut_B.fits")
