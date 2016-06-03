cd ~/desitarget/bin
git checkout mocks
./mock_skypos_stdstars_darktime -R /project/projectdirs/desi/mocks/preliminary/v2_randoms_big.fits -O /project/projectdirs/desi/users/forero/large_mock_test/mtl/
./mock_targets_darktime -Q /project/projectdirs/desi/mocks/preliminary/v2_qso_6.fits -E /project/projectdirs/desi/mocks/preliminary/v2_elg_6.fits -L /project/projectdirs/desi/mocks/preliminary/v2_lrg_6.fits -R /project/projectdirs/desi/mocks/preliminary/v2_randoms_big.fits -O /project/projectdirs/desi/users/forero/large_mock_test/mtl/

cd ~/desisim/bin
git checkout master
./quicksurvey -O /project/projectdirs/desi/users/forero/large_mock_test/ -T /project/projectdirs/desi/users/forero/large_mock_test/mtl/ -f /global/homes/f/forero/fiberassign/bin/./fiberassign -E /project/projectdirs/desi/mocks/preliminary/mtl/lowfat/ -t /global/homes/f/forero/SandboxDESI/end2end/quicksurvey/template_fiberassign.txt -N 3
./quicksurvey_stats -O /project/projectdirs/desi/users/forero/large_mock_test/ -T /project/projectdirs/desi/users/forero/large_mock_test/mtl/ -f /global/homes/f/forero/fiberassign/bin/./fiberassign -E /project/projectdirs/desi/mocks/preliminary/mtl/lowfat/ -t /global/homes/f/forero/SandboxDESI/end2end/quicksurvey/template_fiberassign.txt -N 3

