import DR8 as dr8

dr8.write_initial_mtl_files(output_path="./targets/", program="bright")
dr8.write_initial_mtl_files(output_path="./targets/", program="dark")
dr8.write_sky_files(output_path="./targets/")
