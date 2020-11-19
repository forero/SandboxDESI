import DR9 as dr9

dr9.write_initial_mtl_files(output_path="./targets_dr9/", program="bright")
dr9.write_initial_mtl_files(output_path="./targets_dr9/", program="dark")
dr9.write_sky_files(output_path="./targets_dr9/")
