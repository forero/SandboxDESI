from argparse                      import ArgumentParser
import fitsio
import os

parser = ArgumentParser()
parser.add_argument('--infile',  help='input file',type=str,default=None,required=True, metavar='INFILE')
args     = parser.parse_args()

filenamein = args.infile
filenameout = 'small_'+filenamein
os.remove(filenameout)

print('reading file {}'.format(filenamein))
print('writing file {}'.format(filenameout))

filein =  fitsio.FITS(filenamein,'r')
fileout = fitsio.FITS(filenameout, 'rw')

extnames = ['PRIMARY','FIBERASSIGN','GFA_TARGETS','TARGETS','POTENTIAL_ASSIGNMENTS']

columns = {'FIBERASSIGN':
          ['FIBER', 'TARGETID', 'LOCATION', 'FIBERSTATUS', 
           'LAMBDA_REF' , 'PETAL_LOC', 'TARGET_RA', 
           'TARGET_DEC', 'FA_TARGET' , 'FA_TYPE', 
           'FIBERASSIGN_X', 'FIBERASSIGN_Y'], 
          'TARGETS':
          ['TARGETID', 'RA', 'DEC' , 
           'FA_TARGET', 'FA_TYPE' , 'PRIORITY' , 
           'SUBPRIORITY', 'OBSCONDITIONS' ]}

for extname in extnames:
    header=filein[extname].read_header()

    if extname in columns.keys():
        data = filein[extname].read(columns=columns[extname])
    else:
        data = filein[extname].read()

    if (extname=='PRIMARY'):
        fileout.write(None, header=header, extname=extname)
    else:
        fileout.write(data, extname=extname)
    
filein.close()
fileout.close()