python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00  --tilera 260.07  --tiledec 57.42  --tileid 80862  --faflavor sv1mwclusgaldeep  --priority default --outdir ./sv1scnd # draco
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00   --tilera 198.30  --tiledec 17.50  --tileid 80863  --faflavor sv1mwclusgaldeep  --priority default --outdir ./sv1scnd #M53+NGC5053
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00   --tilera 132.83  --tiledec 11.30  --tileid 80864  --faflavor sv1mwclusgaldeep  --priority default --outdir ./sv1scnd #M67 



# RUNDATE EFFECTIVE_AREA_IN_DEG2
#2020-01-01T00:00:00 7.37 Full fiber reach
#2021-01-17T00:00:00 2.58 Restricted fiber reach
#2021-01-19T00:00:00 3.05 Petal 0
#2021-02-05T00:00:00 4.49 Petals 02,4,5
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00  --tilera 242.75  --tiledec 54.98  --tileid 80865  --faflavor sv1unwisegreen  --priority custom --outdir ./sv1scnd 
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00   --tilera 242.75  --tiledec 54.98  --tileid 80866  --faflavor sv1unwisebluebright  --priority custom --outdir ./sv1scnd 
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00   --tilera 242.75  --tiledec 54.98  --tileid 80867  --faflavor sv1unwisebluefaint  --priority custom --outdir ./sv1scnd

#field         ra      dec         exposure time total
#GREEN1 225   43.25      3 hours
#BLUE1    225   43.25       0.75 hours
#BLUE2   180       0           0.75 hours

# RUNDATE EFFECTIVE_AREA_IN_DEG2
#2020-01-01T00:00:00 7.37 Full fiber reach
#2021-01-17T00:00:00 2.58 Restricted fiber reach
#2021-01-19T00:00:00 3.05 Petal 0
#2021-02-05T00:00:00 4.49 Petals 02,4,5
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00 --tilera 214.86  --tiledec 53.0  --tileid 80868  --faflavor sv1scndhetdex  --priority custom --outdir ./sv1scnd # cfhstls w3
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00 --tilera 166.0  --tiledec 51.5  --tileid 80869  --faflavor sv1scndhetdex  --priority custom --outdir ./sv1scnd
python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.51.0 --rundate 2020-01-01T00:00:00 --tilera 225.0  --tiledec 51.5  --tileid 80870  --faflavor sv1scndhetdex  --priority custom --outdir ./sv1scnd

python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.52.0 --rundate 2020-01-01T00:00:00 --tilera 150.12  --tiledec 2.20  --tileid 080871  --faflavor sv1scndcosmos  --priority custom --outdir ./sv1scnd # cosmos

python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.52.0 --rundate 2020-01-01T00:00:00 --tilera 150.12  --tiledec 2.30  --tileid 080872  --faflavor sv1scndcosmos  --priority custom --noreobs ./sv1scnd/fiberassign-080871.fits.gz --outdir ./sv1scnd

