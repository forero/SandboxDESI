import join as j

for i in ["A", "B", "C", "D", "E"]:
    j.join_fba_targets(targets_file="targets/mtl_cut_{}_dark_south.fits".format(i), 
                       fba_path="fba_run/mtl_dark_south_cut_{}_tiles_cut_{}/".format(i,i), 
                       summary_filename="summary/fba_summary_mtl_dark_south_cut_{}_tiles_cut_{}.fits".format(i,i))
