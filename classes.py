
# Tiles & Map 
# Units and buildings

Red = (255,0,0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)

class terrain:
    """
    Terrain bass class
    Sets the base values for creating a new terrain type
    
    Parameters
    ----------
    name : string
        the name of the particular terrain created
    colour : (int, int, int)
        Takes the colour as (red, green, blue)
        Only used in the base program for debugging     

    """
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

grass = terrain("grass", Green)
sand = terrain("sand", Yellow)
print(grass.colour)
print(sand.colour)


class tile:
    """
    Tile class, contains location, occupied bool and terrain type. 
    
    Parameters
    ----------
    x : int
        x value of the tile
    y : int
        y value of the tile

    Values
    ------
    occupied  : bool
        whether the particular tile is marked as occupied or not
        Defaults to false
    terrain : terrain
        The type of terrain the tile is
        Defaults to grass         
    """
    def __init__(self, x = -1, y = -1):
        self.x = x
        self.y = y
        self.occupied = False
        self.terrain = grass

tileA = tile(0,0)
print("tileA occ = ", tileA.occupied)
tileB = tile(0,1)
tileB.occupied = True
print("tileA occ = ", tileA.occupied)
print("tileB occ = ", tileB.occupied)


class interactable:
    def __init__(self, name, hp=0, att=0, defence=0, location=[]):
        self.name = name
        self.baseHP = hp
        self.baseAtt = att
        self.baseDef = defence
        self.location = location

    def printStats(self):
        print("[ Stats of " + self.name + " ]",
        "------------------------",
        "HP: " + str(self.baseHP),
        "Att: " + str(self.baseAtt),
        "Def: " + str(self.baseDef),
        "------------------------",
        sep='\n')       



class building(interactable):
    def __init__(self, name, xSize, ySize, hp=0, att=0, defence=0, location=[]):
        interactable.__init__(self, name, hp, att, defence, location)
        self.xSize = xSize
        self.ySize = ySize
        self.size = [xSize, ySize] 


    
house = building("house", 2, 2, hp=200, defence=50)
castle = building("castle", 4, 8, hp=500, defence=200)
castle.location = [tileA, tileB]
house.printStats()
print("House location: " + str(house.location))
castle.printStats()
print("castle location: " + str(castle.location))


class unit(interactable):
    def __init__(self, name,hp=0, att=0, defence=0, location=[]):
       interactable.__init__(self, name, hp, att, defence, location)
       self.abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)

warrior = unit("Warrior", hp=50, att=20, defence=25)
warrior.printStats()
