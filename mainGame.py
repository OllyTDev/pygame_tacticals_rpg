from pygame.constants import K_DOWN, K_LEFT, K_RETURN, K_RIGHT, K_UP, K_a, K_d, K_s, K_w
import loadConfig
from classes import colour
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
    playerText = gameFont.render("Player {0}".format(str(starting_player)), 1, colour.BurntUmber)
    pygame.draw.rect(screen, (colour.Black), (50, 5, 200, 35), 2)
    pygame.display.update()
    screen.blit(playerText, (75,10))   
    pygame.display.update()

def changeTurns(screen, currentPlayersTurn, maxPlayers=2):
    
    pygame.draw.rect(screen, (colour.White), (50, 5, 200, 35), 0)
    pygame.draw.rect(screen, (colour.Black), (50, 5, 200, 35), 2)
    pygame.display.update()
    if (currentPlayersTurn == maxPlayers):
        nextPlayersTurn = 1
    else:
        nextPlayersTurn = currentPlayersTurn + 1    

    playerText = gameFont.render("Player {0}".format(str(nextPlayersTurn)), 1, colour.BurntUmber)
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


def main(screen, map):
    # Variable to keep the main loop running

    #for p in players:
    #    print("Player found: ", p)

    currentMap = map

    tiles = loadMap(screen, currentMap)

    nextTurnButtonPosition = (545, 5)
    nextTurnButtonSize = [200, 35]
    nextTurnButton = drawButton(screen, "Next Turn", nextTurnButtonPosition, textColour=colour.BurntUmber, size=nextTurnButtonSize)
    pygame.display.update()

    currentPlayersTurn = 1
    startTurns(screen, currentPlayersTurn)
    
    cursorPos = initializeCursor(screen)
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
                    redrawTile(screen, cursorPos, currentMap)
                    redrawCursor(screen, newPos)
                    cursorPos = newPos
                elif event.key == K_DOWN or event.key == K_s:  
                    newPos = checkNewCursorPos([cursorPos[0],cursorPos[1]+50])
                    redrawTile(screen, cursorPos, currentMap)
                    redrawCursor(screen, newPos)
                    cursorPos = newPos
                elif event.key == K_LEFT or event.key == K_a:
                    newPos = checkNewCursorPos([cursorPos[0]-50,cursorPos[1]])
                    redrawTile(screen, cursorPos, currentMap)
                    redrawCursor(screen, newPos)
                    cursorPos = newPos
                elif event.key == K_RIGHT or event.key == K_d:
                    newPos = checkNewCursorPos([cursorPos[0]+50,cursorPos[1]])
                    redrawTile(screen, cursorPos, currentMap)
                    redrawCursor(screen, newPos)
                    cursorPos = newPos
                elif event.key == K_RETURN:
                    newPos = cursorPos
                    redrawTile(screen, cursorPos, currentMap)
                    change_square(screen, *cursorPos)
                    redrawCursor(screen, newPos)
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
                        redrawTile(screen, cursorPos, currentMap)
                        change_square(screen,*squareClicked)
                        redrawCursor(screen, squareClicked)
                        cursorPos = squareClicked
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print("Left mouse released!")
                if nextTurnButton.collidepoint(pos):
                    currentPlayersTurn = changeTurns(screen, currentPlayersTurn)