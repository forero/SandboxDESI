from argparse                      import ArgumentParser
import fitsio
import os

parser = ArgumentParser()
parser.add_argument('--infile',  help='input file',type=str,default=None,required=True, metavar='INFILE')
parser.add_argument('--outfile',  help='output file',type=str,default=None,required=True, metavar='OUTFILE')

args     = parser.parse_args()

filenamein = args.infile
filenameout = args.outfile
print(type(filenameout))
if os.path.exists(filenameout):
    os.remove(filenameout)

print('reading file {}'.format(filenamein))
print('writing file {}'.format(filenameout))
newtileid = int(filenameout.split('-')[-1].split('.')[0])
print('new tileid {}'.format(newtileid))

filein =  fitsio.FITS(filenamein,'r')
fileout = fitsio.FITS(filenameout, 'rw')

extnames = ['PRIMARY','FIBERASSIGN','SKY_MONITOR','GFA_TARGETS','TARGETS','POTENTIAL_ASSIGNMENTS', 'FASSIGN', 'FTARGETS', 'FAVAIL']

for extname in extnames:
    header=filein[extname].read_header()
    data = filein[extname].read()
        
    header['TILEID'] = newtileid
    if (extname=='PRIMARY'):
        header['FAFLAVOR'] = 'cmxposmapping'
        fileout.write(None, header=header, extname=extname)
    else:
        fileout.write(data, header=header, extname=extname)
    
filein.close()
fileout.close()
