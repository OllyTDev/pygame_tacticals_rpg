import terrains
import classes
import loadConfig

global xLeft, xRight, yTop, yBottom
xLeft = 50
xRight = loadConfig.SCREEN_WIDTH-50
yTop = 50
yBottom = loadConfig.SCREEN_HEIGHT-50

tileArray = []
for y in range (yTop, yBottom, 50):
        for x in range (xLeft, xRight, 50):
            tile = classes.Tile(x,y)
            tileArray.append(tile)
     
grassMap = classes.Map(tileArray) 
for tile in grassMap.tileArray:
    print(tile.terrain.name)

tileArray = []
for y in range (yTop, yBottom, 50):
        for x in range (xLeft, xRight, 50):
            tile = classes.Tile(x,y, terrains.sand)
            tileArray.append(tile)

sandMap = classes.Map(tileArray) 