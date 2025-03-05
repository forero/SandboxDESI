# Start fresh
source /global/common/software/desi/desi_environment.sh main

# Load one of the compatible desimodules versions
module load desimodules/22.5

# Now load the specific fiberassign version
module load fiberassign/5.6.0

python fba_cmx_perlmutter --dr dr9 --dtver 0.49.0 --rundate 2025-03-05T10:00:00+00:00 --seed 77  --tilera 120.0  --tiledec -30.0 --tileid 89000  --faflavor dithprec  --outdir 20250305 &


