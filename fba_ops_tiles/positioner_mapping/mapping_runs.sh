fba_cmx --dr=dr9 --dtver=0.49.0 --rundate=2021-09-07T21:00:00 --seed=77 --faflavor=dithlost --outdir=./ --tilera=343.0 --tiledec=30.0 --tileid=90000

python unique_targets.py 

fiberassign --mtl 090000-unique_targ.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite 

python multiple_target_files.py

fiberassign --mtl 090000-unique_unique_targ_m_00.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082248.fits
gzip  fiberassign-082248.fits

fiberassign --mtl 090000-unique_unique_targ_m_01.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082249.fits
gzip fiberassign-082249.fits

fiberassign --mtl 090000-unique_unique_targ_m_02.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082250.fits
gzip fiberassign-082250.fits

fiberassign --mtl 090000-unique_unique_targ_m_03.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082251.fits
gzip fiberassign-082251.fits

fiberassign --mtl 090000-unique_unique_targ_m_04.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082252.fits
gzip fiberassign-082252.fits

fiberassign --mtl 090000-unique_unique_targ_m_05.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082253.fits
gzip fiberassign-082253.fits 

fiberassign --mtl 090000-unique_unique_targ_m_06.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082254.fits
gzip fiberassign-082254.fits

fiberassign --mtl 090000-unique_unique_targ_m_07.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082255.fits
gzip fiberassign-082255.fits 

fiberassign --mtl 090000-unique_unique_targ_m_08.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082256.fits
gzip fiberassign-082256.fits

fiberassign --mtl 090000-unique_unique_targ_m_09.fits --sky 090000-sky.fits --gfafile 090000-gfa.fits --nstarpetal 0 --footprint 090000-tiles.fits --overwrite
python rename_fba_file.py --infile fiberassign-090000.fits --outfile fiberassign-082257.fits
gzip fiberassign-082257.fits
