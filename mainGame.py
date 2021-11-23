import config

import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Following: https://realpython.com/pygame-a-primer/#basic-pygame-program
#Next thing: https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect

squares = []

def findSquareMouseIsOn(mousePos):
    for square in squares:
        if mousePos < square:
            return square

def initialMap(screen):
    buttons = []
    # Fill the screen with white
    screen.fill((255, 255, 255))
    
    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((45, 45))
    
    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    surf.get_rect()

    # This line says "Draw surf onto the screen at the center"
    for i in range (50, config.SCREEN_HEIGHT-50, 50):
        for j in range (50, config.SCREEN_WIDTH-50, 50):
            b = screen.blit(surf, (i,j))
            buttons.append(b)
            global squares
            squares.append((i,j))

    pygame.display.flip()
    return buttons

def change_square(screen, x, y):
    print("Got here")
    print("X: ", x, " Y: ", y)
    surf = pygame.Surface((45, 45))
    surf.fill((255,0,0))
    screen.blit(surf,(x,y))
    pygame.display.flip()

def main(screen):
    # Variable to keep the main loop running
    running = True
    
    buttons = initialMap(screen)
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
                        # pos is wrong here, we need to see where mouse pos is on what square
                        # basically find which square the mouse is on and pass in those instead
                        squareClicked = findSquareMouseIsOn(pos)
                        change_square(screen,*squareClicked)    
        
