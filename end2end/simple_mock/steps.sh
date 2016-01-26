#create mock data
cd ~/desimock/
./bin/./mock_darktime.py

#pass 0
cd ~/fiberassign
./bin/./fiberassign /global/homes/f/forero/SandboxDESI/end2end/simple_mock/inputs/fiberassign_pass_0.txt 
cd ~/desisim
./bin/./quickcat -f /scratch1/scratchdirs/forero/end2end_mock/fiberassign/pass_0/ -t /scratch1/scratchdirs/forero/end2end_mock/layers/dark_epoch1.txt -T /scratch1/scratchdirs/forero/end2end_mock/mtl/truth_targets_0_mtl_0.fits -o /scratch1/scratchdirs/forero/end2end_mock/quickcat/zcat_pass_0.fits
cd ~/mtl
./bin/./build_mtl -i /scratch1/scratchdirs/forero/end2end_mock/mtl/targets_0_mtl_0.fits -z /scratch1/scratchdirs/forero/end2end_mock/quickcat/zcat_pass_0.fits  -o  /scratch1/scratchdirs/forero/end2end_mock/mtl/targets_0_mtl_1.fits

# pass 1
cd ~/fiberassign
./bin/./assign /global/homes/f/forero/SandboxDESI/end2end/simple_mock/inputs/fiberassign_pass_1.txt
cd ~/desisim
./bin/./quickcat -f /global/cscratch1/sd/forero/simplemock_end2end/fiberdata/pass_1/ -t /global/cscratch1/sd/forero/simplemock_end2end/layerdata/dark_epoch1.txt -T /global/cscratch1/sd/forero/simplemock_end2end/mtldata/truth_objects_ss_sf0.fits -z /global/cscratch1/sd/forero/simplemock_end2end/quickcatdata/zcat_pass_0.fits -o /global/cscratch1/sd/forero/simplemock_end2end/quickcatdata/zcat_pass_1.fits
cd ~/mtl
./bin/./build_mtl -i /global/cscratch1/sd/forero/simplemock_end2end/mtldata/mtl_pass_1.fits -z /global/cscratch1/sd/forero/simplemock_end2end/quickcatdata/zcat_pass_1.fits  -o  /global/cscratch1/sd/forero/simplemock_end2end/mtldata/mtl_pass_2.fits
