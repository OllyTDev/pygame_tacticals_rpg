import pygame
import pygame_menu
import mainGame
import config

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_HEIGHT, config.SCREEN_WIDTH))

def start_the_game():
    mainGame.main(screen)
    pass

def save():
    pass

def load():
    pass

menu = pygame_menu.Menu('Welcome', config.SCREEN_HEIGHT, config.SCREEN_WIDTH,
                       theme=pygame_menu.themes.THEME_DEFAULT)

menu.add.clock(align=pygame_menu.locals.ALIGN_RIGHT)
menu.add.vertical_margin(200)
menu.add.button('Play', start_the_game)
menu.add.button('Save', save)
menu.add.button('Load', load)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
