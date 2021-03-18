from desitarget.targetmask import desi_mask, obsconditions
import fitsio

data_main = fitsio.read("targets/mtl_bright_main_onepct.fits")
print(len(data_main))


data_sv1 = fitsio.read("targets/mtl_bright_sv1_onepct.fits")
print(len(data_sv1))