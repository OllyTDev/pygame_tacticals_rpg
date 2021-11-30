import pygame
from classes import colour

pygame.init()
myfont = pygame.font.SysFont("Arial", 25)

def drawButton(
    screen, 
    text,
    position,
    textColour=colour.Black,
    buttonColour=colour.Black,
    size=(200,35)
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
        Length and size of button, defaults to tuple(200,35)    
    """
    
    
    label = myfont.render(text, 1, textColour)
    text_rect = label.get_rect(center=(position[0]+(size[0]/2), position[1]+(size[1]/2)))
    screen.blit(label, text_rect)
    button = pygame.draw.rect(screen, buttonColour, (position[0], position[1], size[0], size[1]), 2)
    return button