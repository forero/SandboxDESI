./bin/./assign /global/homes/f/forero/SandboxDESI/end2end/simple_mock/inputs/fiberassign_pass_0.txt 

./quickcat -f /global/cscratch1/sd/forero/simplemock_end2end/fiberdata/pass_0/ -t /global/cscratch1/sd/forero/simplemock_end2end/layerdata/dark_epoch0.txt -T /global/cscratch1/sd/forero/simplemock_end2end/mtldata/truth_objects_ss_sf0.fits -o /global/cscratch1/sd/forero/simplemock_end2end/quickcatdata/zcat_pass_0.fits

./build_mtl -i /global/cscratch1/sd/forero/simplemock_end2end/mtldata/objects_ss_sf0.fits -z /global/cscratch1/sd/forero/simplemock_end2end/quickcatdata/zcat_pass_0.fits  -o  /global/cscratch1/sd/forero/simplemock_end2end/mtldata/mtl_pass_1.fits

./bin/./assign /global/homes/f/forero/SandboxDESI/end2end/simple_mock/inputs/fiberassign_pass_1.txt

./quickcat -f /global/cscratch1/sd/forero/simplemock_end2end/fiberdata/pass_1/ -t /global/cscratch1/sd/forero/simplemock_end2end/layerdata/dark_epoch1.txt -T /global/cscratch1/sd/forero/simplemock_end2end/mtldata/truth_objects_ss_sf0.fits -z /global/cscratch1/sd/forero/simplemock_end2end/quickcatdata/zcat_pass_0.fits -o /global/cscratch1/sd/forero/simplemock_end2end/quickcatdata/zcat_pass_1.fits

./build_mtl -i /global/cscratch1/sd/forero/simplemock_end2end/mtldata/mtl_pass_1.fits -z /global/cscratch1/sd/forero/simplemock_end2end/quickcatdata/zcat_pass_1.fits  -o  /global/cscratch1/sd/forero/simplemock_end2end/mtldata/mtl_pass_2.fits
