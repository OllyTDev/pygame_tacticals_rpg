import pygame
import pygame_menu
import loadConfig
#import mainMenu

pygame.init()

def main(screen):

    def start_the_game():
        pass

    def return_to_main_menu():
        ()

    
    running = True
    while running == True:
        menu = pygame_menu.Menu(loadConfig.GAME_NAME, loadConfig.SCREEN_HEIGHT, loadConfig.SCREEN_WIDTH,
                           theme=pygame_menu.themes.THEME_DEFAULT)

        menu.add.clock(align=pygame_menu.locals.ALIGN_RIGHT)
        menu.add.vertical_margin(200)
        menu.add.button('Start', start_the_game)
        menu.add.dropselect("Players",["2","3","4"])
        menu.add.button('Back', return_to_main_menu())

        menu.mainloop(screen)    