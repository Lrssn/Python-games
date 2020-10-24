from utils.createmap import *
from utils.map_utils import *
from mapsquare import *
level = 1
mapsquares = list()
sizex = 100
sizey = 100
map_img = createmap(sizex = 800, sizey = 600, scale = 100, octaves = 4, persistence = 0.3, lacunarity = 2.0, thresholds = (0.2, 0.21, 1.0))
cellular = cellular_automata(sizex,sizey)
layer1 = numpy.zeros((sizex, sizey))
for i in range(sizey):
    subSquares = []
    for j in range(sizex):
        x = Mapsquare(int(map_img[i][j]))
        if map_img[i][j] == 2 and cellular[i][j] == 1:
            x.add_layer(1)
        else:
            x.add_layer(0)
        subSquares.append(x)
       
    mapsquares.append(subSquares)
mapname = "map" + str(level) + ".map"
savemap(mapname, mapsquares, sizex, sizey)
print("map "  + str(mapname) +  " saved")