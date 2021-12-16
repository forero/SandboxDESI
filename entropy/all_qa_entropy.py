from argparse import ArgumentParser
import image_entropy as ient
import pandas as pd
import fitsio
import os



def list_exps(date):
    exps_daily = pd.read_csv("/global/cfs/cdirs/desi/spectro/redux/daily/exposures-daily.csv")
    #print(exps_daily.keys())
    ii = (exps_daily["NIGHT"]==date)
    #print(exps_daily["NIGHT"][ii])
    exps_daily = exps_daily[ii]
    return exps_daily
    
def read_sky_sframe(sframe_file):
    try:
        h = fitsio.FITS(sframe_file)
        sel = h["FIBERMAP"]["OBJTYPE"].read() == "SKY"
        sky = h["FLUX"].read()[sel,:]
    except:
        sky = None
    return sky

def compute_sframe_entropy(output_path, exp_path, date, expid):
    n_petals = 10
    bands = ['b', 'r', 'z']
    summary = {}
    summary['band'] = []
    summary['petal'] = []
    summary['entropy'] = []
    summary['expid'] = []
    summary['night'] = []
    for i in range(n_petals):
        for band in bands:
            filename = '{}/{}/{:08d}/sframe-{}{}-{:08d}.fits'.format(exp_path, date, expid, band, i, expid)
            sky_petal = read_sky_sframe(filename)
            if sky_petal is not None:
                proba = ient.compute_probability_distribution_2D(sky_petal)
                entropy =  ient.compute_entropy(proba)
                summary['band'].append(band)
                summary['petal'].append(i)
                summary['entropy'].append(entropy)
                summary['expid'].append(expid)
                summary['night'].append(date)
                print(date, expid, band, i, entropy)
    entropy_df = pd.DataFrame.from_dict(summary)
    filename = 'entropy_sky_sframe_{}_{:08d}.csv'.format(date, expid)
    
    os.makedirs(output_path, exist_ok=True) 
    entropy_df.to_csv(os.path.join(output_path,filename))
    
    print(summary)
    
def main():
    print(args)
    exp_path = "/global/cfs/cdirs/desi/spectro/redux/daily/exposures/"
    exps = list_exps(int(args.date))
    dates = list(exps["NIGHT"])
    expids = list(exps["EXPID"])
    for date, expid in zip(dates, expids):
        compute_sframe_entropy(os.path.join(args.outdir, str(date)), exp_path, date, expid)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--date", help="input date (e.g., 20211202)", type=int,default=None,required=True)
    parser.add_argument("--outdir", help="output directory",type=str,default="./",required=False)
    args = parser.parse_args()
    
    main()