
from pygame import image
import terrains
# Tiles & Map 
# Units and buildings

class colour():
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)
    SelectionBlue = (139, 217, 247)
    Yellow = (255, 255, 0)
    BurntUmber = (110,38,14)
    LightBlue = (173,216,230)

class Tile:
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
    def __init__(self, x = -1, y = -1, terrain=terrains.grass):
        self.x = x
        self.y = y
        self.pos = [x,y]
        self.occupied = False
        self.terrain = terrain

class Map:
    """
    A map should be an array of tiles
    """
    def __init__(self, tileArray):
        self.tileArray = tileArray

class Interactable:
    def __init__(self, name, hp=0, att=0, defence=0, location=[], startImage="Asset/Units/BlankUnitFrontFrame1.png", imageList=["Asset/Units/BlankUnitFrontFrame1.png"], player=0):
        self.name = name
        self.baseHP = hp
        self.baseAtt = att
        self.baseDef = defence
        self.location = location
        self.image = startImage
        self.imageList = imageList
        self.player = player

    def printStats(self):
        print("[ Stats of " + self.name + " ]",
        "------------------------",
        "HP: " + str(self.baseHP),
        "Att: " + str(self.baseAtt),
        "Def: " + str(self.baseDef),
        "------------------------",
        sep='\n')       



class Building(Interactable):
    def __init__(self, name, xSize, ySize, hp=0, att=0, defence=0, location=[], startImage="Asset/Units/BlankUnitFrontFrame1.png", imageList=[], player=0):
        Interactable.__init__(self, name, hp, att, defence, location, startImage, imageList, player)
        self.xSize = xSize
        self.ySize = ySize
        self.size = [xSize, ySize]


    
house = Building("house", 2, 2, hp=200, defence=50)
castle = Building("castle", 4, 8, hp=500, defence=200)
house.printStats()
print("House location: " + str(house.location))
castle.printStats()
print("castle location: " + str(castle.location))


class Unit(Interactable):
    def __init__(self, name,hp=0, att=0, defence=0, location=[], startImage="Asset/Units/BlankUnitFrontFrame1.png", imageList=[], player=0):
        Interactable.__init__(self, name, hp, att, defence, location, startImage, imageList, player)
        self.abilities = []
        self.move_frame = 0
        

    def add_ability(self, ability):
        self.abilities.append(ability)

    def update(self):
         # Return to base frame if at end of movement sequence 
        if self.move_frame >= len(self.imageList):
            self.move_frame = 0
            return
        # Move the character to the next frame if conditions are met
        self.image = self.imageList[int(self.move_frame)]
        self.move_frame += 0.001      

warrior = Unit("Warrior", hp=50, att=20, defence=25)
warrior.printStats()

class Player():
    
     def __init__(self, name, colour, team, faction):
        self.name = name
        self.colour = colour
        self.team = team
        self.faction = faction