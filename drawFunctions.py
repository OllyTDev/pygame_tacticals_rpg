import pygame
from pygame import draw
from classes import colour

pygame.init()
myfont = pygame.font.SysFont("Arial", 25)

def checkTextSize(text, buffer_X, buffer_Y):
    text_width, text_height = myfont.size(text)
    return [text_width+buffer_X, text_height+buffer_Y]

def drawButton(
    screen, 
    text,
    position,
    textColour=colour.Black,
    buttonColour=colour.Black,
    size=[0,0],
    buffer_X = 25,
    buffer_Y = 10
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
    
    calculatedSize = checkTextSize(text,buffer_X,buffer_Y)
    if (size == [0,0]):
        size = calculatedSize

    label = myfont.render(text, 1, textColour)
    text_rect = label.get_rect(center=(position[0]+(size[0]/2), position[1]+(size[1]/2)))
    screen.blit(label, text_rect)
    button = drawOutlineRect(screen, position, buttonColour, size)
    return button

def drawOutlineRect(screen, position, buttonColour, size, width=2):
    b = pygame.draw.rect(screen, buttonColour, (position[0], position[1], size[0], size[1]), width)
    return b

class column():
    def __init__(self, header, type="str", buffer_X = 25, buffer_Y = 10):
        self.header = header
        self.type = type
        self.buffer_X = buffer_X
        self.buffer_Y = buffer_Y

def drawHeaders(screen, columns, position, currentXDrawPos, columnStartandSize_X):
    for column in columns:
        b = drawButton(screen, column.header, (currentXDrawPos, position[1]), buffer_X=column.buffer_X, buffer_Y=column.buffer_Y)
        columnStartandSize_X.update({column.header: (currentXDrawPos, b.width)}) # Gonna give us data like: colour: 185 & faction: 491
        currentXDrawPos = currentXDrawPos + b.size[0] - 1
    currentRowYPos = position[1] + b.size[1] - 1
    return currentRowYPos

class row():
    def __init__(self):
        self.data = {}

    def addData(self,keyValues):
        for pair in keyValues:
            self.data.update({pair[0]:pair[1]})


def drawRowByType(screen, columnType, value, pos, buttonSize):
    if (columnType == "colour"):
        b = drawOutlineRect(screen, pos, colour.Black, size=buttonSize) #Draw the rect button behind it
        if (value != colour.Black):
            drawOutlineRect(screen, (pos[0]+2, pos[1]+2), value, size=(buttonSize[0]-3, buttonSize[1]-3), width=0) #-3 cus we want it smaller
        else:    
            drawButton(screen, "N/A", pos, size=buttonSize)
    elif (columnType == "str"):
        b = drawButton(screen, value, pos, size=buttonSize)
    else:
        b = drawButton(screen, str(value), pos, size=buttonSize)       
    return b

def drawRows(screen, rows, columnStartPosandSizeDict, currentRowYPos, columnTypeDict):
    buttons = []
    for row in rows:
        for column, value in row.data.items():
            pos = [columnStartPosandSizeDict[column][0], currentRowYPos] 
            calcedSize = checkTextSize(str(value), 25, 10)
            buttonCalcedSize = (columnStartPosandSizeDict[column][1]-1,calcedSize[1])
            b = drawRowByType(screen, columnTypeDict[column], value, pos, buttonCalcedSize)
            buttons.append(b)
        currentRowYPos = currentRowYPos + b.size[1] - 1
    return buttons    

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

    currentXDrawPos = position[0]
    columnStartPosandSizeDict = {}
    buttons = []
    
    currentRowYPos = drawHeaders(screen, columns, position, currentXDrawPos, columnStartPosandSizeDict)

    columnTypeDict = {}
    for column in columns:
        columnTypeDict.update({column.header: column.type})

    buttons = drawRows(screen, rows, columnStartPosandSizeDict, currentRowYPos, columnTypeDict)
    return buttons

