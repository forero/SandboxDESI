all: summary_rr_entropy_daily.csv low_entropy_rr_example.pdf high_entropy_rr_example.pdf

summary_rr_entropy_daily.csv: script_daily.py
	python script_daily.py
	
low_entropy_rr_example.pdf: /global/cfs/cdirs/desi/spectro/redux/daily/tiles/cumulative/26056/20220221/redrock-1-26056-thru20220221.fits plot_entropy.py
	python plot_entropy.py

high_entropy_rr_example.pdf: /global/cfs/cdirs/desi/spectro/redux/daily/tiles/cumulative/26056/20220221/redrock-1-26056-thru20220221.fits plot_entropy.py
	python plot_entropy.py
