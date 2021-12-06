import pygame
import mainGame
import maps
from classes import colour
from drawFunctions import column, row, drawButton, drawTable
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

def start(screen):
    mainGame.main(screen, maps.sandMap)
    #mainGame.main(screen, maps.grassMap)

def quit():
    global running
    running = False

def main(screen):

    myfont = pygame.font.SysFont("Arial", 15)
    screen.fill(colour.LightBlue)

    def intialClassTables():
        skirmishColumns = [column("Colour",(colour), buffer_X=10), column("Player", buffer_X=75), column("Faction", buffer_X=75), column("Team", buffer_X=50)]
                    
        values = [("Colour",(colour.Red)), ("Player", "Player1"), ("Faction", "Faction1"), ("Team", "team1") ]
        values2 = [("Colour",(colour.Blue)), ("Player", "Player2"), ("Faction", "Faction2"), ("Team", "team2") ]
        row1 = row()
        row1.addData(values)
        row2 = row()
        row2.addData(values2)
        rows = [row1, row2]

        drawTable(screen, skirmishColumns, rows, (100,100))
        pygame.display.update()


    defaultButtonSize = [200, 35]
    startButton = drawButton(screen, "Start", (500, 500), size = defaultButtonSize)
    backButton = drawButton(screen, "Back",  (100, 500), size = defaultButtonSize)

    global players
    players = 2
    intialClassTables()
    #initialTable()
    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if backButton.collidepoint(pos):
                    quit()
                elif startButton.collidepoint(pos):
                    start(screen)    
                #for b in buttons:
                #    if b.collidepoint(pos):
                #        print("found a button?")
    
        


