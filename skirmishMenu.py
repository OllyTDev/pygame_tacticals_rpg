import pygame
from pygame import surface
import pygame_menu
import loadConfig
from mainGame import changeTurns
from classes import colour
from drawFunctions import drawButton
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()




def main(screen):

    

    myfont = pygame.font.SysFont("monospace", 15)
    screen.fill(colour.LightBlue)

    def start_the_game():
        change_table()
        #Confirm before start

    global tableCurrentRows
    tableCurrentRows = 1

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

    def quit():
        global running
        running = False

    backButton = drawButton(screen, "Back",  (100, 500))

    global players
    players = 2
    buttons = change_table()
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
                for b in buttons:
                    if b.collidepoint(pos):
                        print("found a button?")
    
        


