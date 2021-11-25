import config
from classes import colour
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


#Following: https://realpython.com/pygame-a-primer/#basic-pygame-program


squares = []
xList, yList = [],[]

def findCoordinate(coordinateList, target):
    i = 0
    revList = list(reversed(coordinateList))
    while (i < len(revList)):
        if(revList[i] < target):
            return revList[i]
        else: 
            i = i + 1    

def findSquareMouseIsOn(mousePos):

    xPos = findCoordinate(xList,mousePos[0])
    yPos = findCoordinate(yList,mousePos[1])
        
    return (xPos, yPos)

def initialMap(screen):
    buttons = []
    # Fill the screen with white
    screen.fill(colour.White)
    
    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((45, 45))
    
    # Give the surface a color to separate it from the background
    surf.fill(colour.Black)
    surf.get_rect()

    # This line says "Draw surf onto the screen at the center"
    for i in range (50, config.SCREEN_HEIGHT-50, 50):
        for j in range (50, config.SCREEN_WIDTH-50, 50):
            b = screen.blit(surf, (i,j))
            buttons.append(b)
            global squares
            squares.append((i,j))
            createMapLists()

    pygame.display.flip()
    return buttons

def initialTacticsUI(screen):

    pygame.draw.rect(screen, (colour.Black), (400, 5, 200, 35), 2)
    pygame.display.update()
    
    #surf = pygame.Surface((300, 50))
    #screen.blit(surf, (400,0))

    font = pygame.font.SysFont('Arial', 25)
    screen.blit(font.render('Next Turn', True, (colour.BurntUmber)), (440, 10))
    pygame.display.update()

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

def change_square(screen, x, y):
    surf = pygame.Surface((45, 45))
    surf.fill((255,0,0))
    screen.blit(surf,(x,y))
    pygame.display.flip()

def main(screen):
    # Variable to keep the main loop running
    running = True
    
    buttons = initialMap(screen)
    initialTacticsUI(screen)
    # Main loop
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                print("mouse left clicked at ", pos)
                ## check if cursor is on button ##
                for b in buttons:
                    if b.collidepoint(pos):
                        squareClicked = findSquareMouseIsOn(pos)
                        change_square(screen,*squareClicked)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("Left mouse released!")                
        
