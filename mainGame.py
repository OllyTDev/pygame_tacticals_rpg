from pygame import draw
from pygame.constants import K_DOWN, K_LEFT, K_RETURN, K_RIGHT, K_UP, K_a, K_d, K_s, K_w
import loadConfig
from classes import Player, colour, Unit
import pygame
from drawFunctions import drawButton
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

squares = []
xList, yList = [],[]
gameFont = pygame.font.SysFont('Arial', 25)

global xLeft, xRight, yTop, yBottom
xLeft = 50
xRight = loadConfig.SCREEN_WIDTH-50
yTop = 50
yBottom = loadConfig.SCREEN_HEIGHT-50

baseUnit_ani = [pygame.image.load("Asset/Units/BlankUnitFrontFrame1.png"), pygame.image.load("Asset/Units/BlankUnitFrontFrame2.png")]

def getPosFromTileLocation(tileTuple):
    """
    Takes a tileTuple e.g. [1,1] and gives us the position of the tile [1,1]
    """
    xPos = xList[tileTuple[0]]
    yPos = yList[tileTuple[1]]

    return [xPos, yPos]

def findCoordinate(coordinateList, target):
    i = 0
    revList = list(reversed(coordinateList))
    while (i < len(revList)):
        if(revList[i] <= target):
            return revList[i]
        else: 
            i = i + 1    

def findSquareMouseIsOn(mousePos):

    xPos = findCoordinate(xList,mousePos[0])
    yPos = findCoordinate(yList,mousePos[1])
        
    return [xPos, yPos]

def drawTile(screen, tile):
    tilePos = [tile.x, tile.y]
    tileImage = pygame.image.load(tile.terrain.image)
    screen.blit(tileImage, tilePos)
   

def loadMap(screen, map):
    buttons = []
    buttons = initialGridmap(screen)
    # Fill the screen with white
    screen.fill(colour.White)
    
    #for each tile in the map
    #draw the tile
    for tile in map.tileArray:
        drawTile(screen,tile)

    pygame.display.flip()
    return buttons

def initialGridmap(screen):
    buttons = []
    # Fill the screen with white
    screen.fill(colour.White)
    
    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50, 50))
    
    # Give the surface a color to separate it from the background
    surf.fill(colour.Black)
    surf.get_rect()
    
    global xLeft, xRight, yTop, yBottom
    # This line says "Draw surf onto the screen at the center"
    for y in range (yTop, yBottom, 50):
        for x in range (xLeft, xRight, 50):
            b = screen.blit(surf, (x,y))
            buttons.append(b)
            global squares
            squares.append((x,y))
            createMapLists()

    pygame.display.flip()
    return buttons

def createMapLists():
    i = 0
    tempXlist, tempYList = [],[]
    global xList, yList
    while (i < len(squares)):
        tempXlist.append(squares[i][0])
        tempYList.append(squares[i][1])
        i = i + 1

    xList = list(dict.fromkeys(tempXlist))
    yList = list(dict.fromkeys(tempYList))

def startTurns(screen, starting_player):
    """
    Starts and renders the current player button. 
    
    Parameters
    ---------
    Screen: Screen
        The screen to render on

    Starting player: player
        Starting player stored as a classes.player    
    """
    playerText = gameFont.render(starting_player.name, 1, colour.BurntUmber)
    pygame.draw.rect(screen, (colour.Black), (50, 5, 200, 35), 2)
    pygame.display.update()
    screen.blit(playerText, (75,10))   
    pygame.display.update()

def changeTurns(screen, currentPlayersTurn, players):
    """
    Finds the current player in the list and then iterates to the next player in the list and renders the next player.
    If the player is last in the list, it should loop around the list and draw player 1 again.
    
    Parameters
    ---------
    Screen: Screen
        The screen to render on

    currentPlayersTurn: player
        current players whos turn it currently is stored as a classes.player

    players: List[player]
        list of current games players 
    """
    pygame.draw.rect(screen, (colour.White), (50, 5, 200, 35), 0)
    pygame.draw.rect(screen, (colour.Black), (50, 5, 200, 35), 2)
    pygame.display.update()
    drawPlayer = False
    drawn = False
    while (drawn == False):
        for p in players:
            if (drawPlayer == True and drawn == False): 
                #if found the current player in the list AND we haven't drawn a new label yet, draw the next player
                print("drawing p.name: ", p.name)
                playerText = gameFont.render(p.name, 1, colour.BurntUmber)
                nextPlayersTurn = p
                drawn = True
            elif (p == currentPlayersTurn): 
                #if find current player
                drawPlayer = True
                #mark the next player to be drawn
    screen.blit(playerText, (75,10))
    pygame.display.update()
    return nextPlayersTurn

def findTileOnMap(targetPos, map):
    for tile in map.tileArray:
        if (tile.pos == targetPos):
            return tile


#function might be useful for drawing a tileSized square on screen
def change_square(screen, x, y, tileColour=colour.Red):
    surf = pygame.Surface((45, 45))
    surf.set_alpha(100)
    surf.fill(tileColour)
    screen.blit(surf,(x+3,y+3))
    pygame.display.flip()

def initializeCursor(screen):
    cursorPos = [50,50]
    cursorImg = pygame.image.load("Asset\Cursor.png")
    screen.blit(cursorImg, (50,50))
    return cursorPos


def redrawTile(screen, pos, map):
    
    #from oldPos, find tile, find tile image, fill in tile with tile image
    tile = findTileOnMap(pos, map)
    tileImage = pygame.image.load(tile.terrain.image)
    screen.blit(tileImage, pos)
    
def redrawCursor(screen, newPos):
    #draw the cursor at the new position
    cursorImg = pygame.image.load("Asset\Cursor.png")
    screen.blit(cursorImg, newPos)
    pygame.display.update()
    return newPos

def checkNewCursorPos(pos):
    
    xPos = pos[0]
    yPos = pos[1]
    global xLeft, xRight, yTop, yBottom
    mapLeft = xLeft
    mapRight = xRight-50
    mapTop = yTop
    mapBottom = yBottom-50
    if(xPos < mapLeft):
        #going off the left of the screen
        pos = [xLeft, yPos]
    elif (xPos > mapRight):
        #going off right of screen
        pos = [mapRight, yPos]
    elif (yPos < mapTop):
        #going off top of screen
        pos = [xPos, yTop]
    elif (yPos > mapBottom):
        #going off bottom of screen   
        pos = [xPos, mapBottom]
    return pos

def drawUnits(screen, unitList):

    for unit in unitList:
        unitPos = getPosFromTileLocation(unit.location)
        unitImage = pygame.image.load(unit.image)
        screen.blit(unitImage, unitPos)

def spawnUnits(players):
    unitList = []
    baseUnitImageList = ["Asset/Units/BlankUnitFrontFrame1.png", "Asset/Units/BlankUnitFrontFrame2.png"]
    i = 0
    for p in players:
        i = i + 1
        if (i == 1):
            starterUnit = Unit("Warrior", hp=50, att=20, defence=25, location=[1,1], imageList=baseUnitImageList, player=p)
        elif (i == 2):
            starterUnit = Unit("Warrior", hp=50, att=20, defence=25, location=[10,1], imageList=baseUnitImageList, player=p)
        elif (i == 3):
            starterUnit = Unit("Warrior", hp=50, att=20, defence=25, location=[1,8], imageList=baseUnitImageList, player=p)
        elif (i == 4):
            starterUnit = Unit("Warrior", hp=50, att=20, defence=25, location=[10,8], imageList=baseUnitImageList, player=p)              
        unitList.append(starterUnit)

    return unitList    


def redrawMap(screen, currentMap, cursorPos, unitList, newPos, changeSquare=False):
    redrawTile(screen, cursorPos, currentMap)
    drawUnits(screen, unitList)
    if (changeSquare):
        change_square(screen, *cursorPos)   
    redrawCursor(screen, newPos)

def redrawMapAfterClick(screen, currentMap, unitList, cursorPos, squareClicked):
    redrawTile(screen, cursorPos, currentMap)
    drawUnits(screen, unitList)
    change_square(screen,*squareClicked)
    redrawCursor(screen, squareClicked)

def isCursorOverUnit(cursorPos, unitList, redrawMap):
    for unit in unitList:
        unitPos = getPosFromTileLocation(unit.location)
        if(cursorPos == unitPos):
            redrawMap
            unit.update()


def main(screen, map, players):
    # Variable to keep the main loop running
    currentMap = map

    tiles = loadMap(screen, currentMap)

    nextTurnButtonPosition = (545, 5)
    nextTurnButtonSize = [200, 35]
    nextTurnButton = drawButton(screen, "Next Turn", nextTurnButtonPosition, textColour=colour.BurntUmber, size=nextTurnButtonSize)
    pygame.display.update()

    currentPlayersTurn = players[0]
    startTurns(screen, currentPlayersTurn)

    unitList = spawnUnits(players)
    drawUnits(screen, unitList)

    cursorPos = initializeCursor(screen)
    newPos = cursorPos
    pygame.display.update()

    running = True
    # Main loop
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP or event.key == K_w:
                    newPos = checkNewCursorPos([cursorPos[0],cursorPos[1]-50])
                    redrawMap(screen, currentMap, cursorPos, unitList, newPos)
                    cursorPos = newPos
                elif event.key == K_DOWN or event.key == K_s:  
                    newPos = checkNewCursorPos([cursorPos[0],cursorPos[1]+50])
                    redrawMap(screen, currentMap, cursorPos, unitList, newPos)
                    cursorPos = newPos
                elif event.key == K_LEFT or event.key == K_a:
                    newPos = checkNewCursorPos([cursorPos[0]-50,cursorPos[1]])
                    redrawMap(screen, currentMap, cursorPos, unitList, newPos)
                    cursorPos = newPos
                elif event.key == K_RIGHT or event.key == K_d:
                    newPos = checkNewCursorPos([cursorPos[0]+50,cursorPos[1]])
                    redrawMap(screen, currentMap, cursorPos, unitList, newPos)
                    cursorPos = newPos
                elif event.key == K_RETURN:
                    newPos = cursorPos
                    redrawMap(screen, currentMap, cursorPos, unitList, newPos, changeSquare=True)
                    cursorPos = newPos
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                print("mouse left clicked at ", pos)
                ## check if cursor is on button ##
                for t in tiles:
                    if t.collidepoint(pos):
                        squareClicked = findSquareMouseIsOn(pos)
                        print("squareClicked: ", str(squareClicked))
                        redrawMapAfterClick(screen, currentMap, unitList, cursorPos, squareClicked)
                        cursorPos = squareClicked
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print("Left mouse released!")
                if nextTurnButton.collidepoint(pos):
                    currentPlayersTurn = changeTurns(screen, currentPlayersTurn, players)          
        isCursorOverUnit(cursorPos, unitList, redrawMap(screen, currentMap, cursorPos, unitList, newPos))
