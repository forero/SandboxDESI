import join as j

#j.join_fba_targets(targets_file="targets_dr9/bright_full.fits",
#                   fba_path="fba_run_dr9/full_run_bright/", 
#                   summary_filename="summary_dr9/fba_summary_bright_full_dr9.fits")

#j.join_fba_targets(targets_file="targets_dr9/dark_full.fits",
#                   fba_path="fba_run_dr9/full_run_dark/", 
#                   summary_filename="summary_dr9/fba_summary_dark_full_dr9.fits")


j.join_fba_targets(targets_file="targets_dr9/dark_full.fits",
                   fba_path="fba_run_dr9/full_run_dark/", 
                   summary_filename="summary_dr9/fba_summary_dark_full_dr9_nopetal_3.fits", exclude_petal=3)