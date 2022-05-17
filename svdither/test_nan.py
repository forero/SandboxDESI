import glob
import fitsio
import pandas as pd

files = glob.glob("*/fiberassign-*.fits.gz")

for f in files:
    df = pd.DataFrame(fitsio.read(f))
    a = df[df.isna().any(axis=1)][['PETAL_LOC','DEVICE_LOC','TARGET_RA','TARGET_DEC']]
    print(f)
    print(a)
