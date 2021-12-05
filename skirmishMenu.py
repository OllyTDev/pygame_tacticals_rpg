import pygame
import mainGame
import maps
from classes import colour
from drawFunctions import column, drawButton, drawTable
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

def start(screen):
    mainGame.main(screen, maps.grassMap)

def quit():
    global running
    running = False

def main(screen):

    myfont = pygame.font.SysFont("Arial", 15)
    screen.fill(colour.LightBlue)

    global tableCurrentRows
    tableCurrentRows = 1
    def intialClassTables():
        skirmishColumns = [column("Colour",(colour)), column("Player"), column("Faction"), column("Team")]
        drawTable(screen,skirmishColumns,"",(100,100))
        pygame.display.update()

    def initialTable():
        i = 0 
        while (i < 4):
            i = i + 1
            match i:
                case 1:
                    drawButton(screen, "Colour", (((100*i), 100)),size=[150,25])
                    #label = myfont.render("Colour", 1, colour.Black)
                    #screen.blit(label, (100+(100*i), 100))
                case 2:
                    label = myfont.render("Player", 1, colour.Black)
                    screen.blit(label, (100+(100*i), 100))
                case 3:
                    label = myfont.render("Faction", 1, colour.Black)
                    screen.blit(label, (100+(100*i), 100))   
                case 4:
                    label = myfont.render("Team", 1, colour.Black)
                    screen.blit(label, (100+(100*i), 100))
                case _:
                    return   
            pygame.display.update()           

    def change_table():
        
        buttons = []
        print("Change table")
        global players
        print(players)
        global tableCurrentRows

        while (tableCurrentRows <= int(players)):
            entry = 0
            while (entry <= 2):
                label = myfont.render("Test!", 1, colour.Black)
                b = screen.blit(label, (100+(100*entry), 100+(tableCurrentRows*100)))
                buttons.append(b)
                entry = entry+1
            tableCurrentRows = tableCurrentRows + 1        

        pygame.display.update() 
        return buttons

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
    
        


