import numpy as np

def write_tile_file(desitiles="desi-tiles.par", epochtiles="lowfat-desi-tiles.par"):
    filein = open(desitiles, "r")
    tilelines = filein.readlines()
    filein.close()

    
    fileout = open(epochtiles, "w")
    for line in tilelines:
        words = line.split()
        if(len(words) < 5):
            fileout.write("{}".format(line))
        else:
            tile = int(words[1])
            in_desi = int(words[4])
            ra = float(words[2])
            dec = float(words[3])
            if in_desi == 0:
                raise NameError('TileNotInDESI')
            if (ra>=150.0) & (ra<=200.0) & (dec<=20.0) & (dec>=0.0):
                fileout.write("{}".format(line))
    fileout.close()

desitiles = "/project/projectdirs/desi/software/edison/desimodel/0.3.1/data/footprint/desi-tiles.par"
write_tile_file(desitiles=desitiles)
