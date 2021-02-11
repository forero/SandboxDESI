python ~/fiberassign/bin/fba_sv1  --dr dr9 --dtver 0.50.0 --rundate 2021-02-05T00:00:00  --tilera 150.12  --tiledec 2.20  --tileid 82000  --faflavor sv1lbg  --priority default --outdir ./sv1lbg # cosmos

#These are the secondary programs for the Cosmos field, in order of priority:
#==========================================================
#- ISM_CGM_QGP
#- HSC_HIZ_SNE
#- LBG_TOMOG
#- Hitherto not-bit-defined Clauds program (equal priority to LBG_TOMOG?)

#These are the secondary programs for the CFHTLS-W3 field, in order of priority:
#=============================================================
#- HETDEX_HP
#- HETDEX_MAIN  (this will need to be downsampled by a factor of 5x in desitarget before we run fiberassign)
#- LBG_TOMOG
#- Hitherto not-bit-defined Clauds program (equal priority to LBG_TOMOG?)