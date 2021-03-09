python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00  --tilera 242.75  --tiledec 54.98  --tileid 82000  --faflavor sv1unwisegreen  --priority custom --outdir ./sv1unwise 
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00   --tilera 242.75  --tiledec 54.98  --tileid 82001  --faflavor sv1unwisebluebright  --priority default --outdir ./sv1unwise 
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00   --tilera 242.75  --tiledec 54.98  --tileid 82002  --faflavor sv1unwisebluefaint  --priority default --outdir ./sv1unwise

#field         ra      dec         exposure time total
#GREEN1 225   43.25      3 hours
#BLUE1    225   43.25       0.75 hours
#BLUE2   180       0           0.75 hours

# RUNDATE EFFECTIVE_AREA_IN_DEG2
#2020-01-01T00:00:00 7.37 Full fiber reach
#2021-01-17T00:00:00 2.58 Restricted fiber reach
#2021-01-19T00:00:00 3.05 Petal 0
#2021-02-05T00:00:00 4.49 Petals 02,4,5
