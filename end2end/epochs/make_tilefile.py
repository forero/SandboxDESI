import numpy as np

def write_epoch_file(desitiles="desi-tiles.par", epochfile="dark_epoch0.txt", epochtiles="epoch-desi-tiles.par"):
    filein = open(desitiles, "r")
    tilelines = filein.readlines()
    filein.close()
    tiles = np.loadtxt(epochfile)
    
    fileout = open(epochtiles, "w")
    for line in tilelines:
        words = line.split()
        if(len(words) < 5):
            fileout.write("{}".format(line))
        else:
            tile = int(words[1])
            in_desi = int(words[4])
            if in_desi == 0:
                raise NameError('TileNotInDESI')
            if tile in tiles:
                fileout.write("{}".format(line))
    fileout.close()

def test():
    desitiles = "/project/projectdirs/desi/software/edison/desimodel/0.3.1/data/footprint/desi-tiles.par"
    epochfile = "/project/projectdirs/desi/datachallenge/Argonne2015/opsim2.1/epochs/dark_epoch0.txt"
    import glob
    epochfiles = glob.glob("/project/projectdirs/desi/datachallenge/Argonne2015/opsim2.1/epochs/dark_epoch*.txt")

    for epochfile in epochfiles:
        epochtiles = epochfile.split("/")[-1].replace("txt", "par")
        write_epoch_file(desitiles=desitiles, epochfile=epochfile, epochtiles=epochtiles)

