import pygame
from pygame import draw
from classes import colour

pygame.init()
myfont = pygame.font.SysFont("Arial", 25)

def checkTextSize(text, bufferX, bufferY):
    text_width, text_height = myfont.size(text)
    return [text_width+bufferX, text_height+bufferY]

def drawButton(
    screen, 
    text,
    position,
    textColour=colour.Black,
    buttonColour=colour.Black,
    size=[0,0],
    bufferX = 25,
    bufferY = 10
    ):
    """
    Function to help creation consitent buttons
        
    Parameters
    ----------------
    screen: screen to draw on

    text: str
        Text displayed on screen

    position: tuple(int, int)
        tuple(x position, y position)
        Position both button and label will be drawn at  

    textColour: (int, int, int)    
        colour of the text on the button

    buttonColour: (int, int, int)    
        colour of the button itself    
    
    size:  tuple (int, int)
        tuple(x length, y length)
        Length and size of button, defaults to be calculated if no size given
    """
    
    calculatedSize = checkTextSize(text,bufferX,bufferY)
    if (size == [0,0]):
        size = calculatedSize

    label = myfont.render(text, 1, textColour)
    text_rect = label.get_rect(center=(position[0]+(size[0]/2), position[1]+(size[1]/2)))
    screen.blit(label, text_rect)
    button = pygame.draw.rect(screen, buttonColour, (position[0], position[1], size[0], size[1]), 2)
    return button

class column():
    def __init__(self, header, type="str"):
        self.header = header
        self.type = type

skirmishColumns = [column("Colour",(colour)), column("Player"), column("Faction"), column("Team")]

class row():
    def __init__(self):
        self.data = {}

    def addData(self,keyValues):
        for pair in keyValues:
            self.data.update({pair[0]:pair[1]})
            
values = [("Colour",(colour.Red)), ("Player", "Player1"), ("Faction", "Faction1"), ("Team", "team1") ]
values2 = [("Colour",(colour.Blue)), ("Player", "Player2"), ("Faction", "Faction2"), ("Team", "team2") ]
row1 = row().addData(values)
row2 = row().addData(values)
rows = [row1, row2]


def drawTable(screen, columns, rows, position):
    """
    Draw a table on screen

    Parameters
    ----------------
    screen: screen to draw on

    column: List (columns)
        List of individual columns (a custom class)
        Each column is made up of the header of the column (str)
    
    rows: List (rows)
        List of rows to draw
        Each row contains the data for each column stored as a dict       

    position: tuple(int, int)  
        Position to start drawing the table at
        stored as (x, y)  
    """
    print("DrawTable function")
    currentXDrawPos = position[0]

    for column in columns:
        print("Draw the column:", column)
        b = drawButton(screen, column.header, (currentXDrawPos, position[1]))
        currentXDrawPos = currentXDrawPos + b.size[0] 