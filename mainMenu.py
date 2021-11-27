import pygame
import pygame_menu
import mainGame
import loadConfig
import skirmishMenu

pygame.init()

screen = pygame.display.set_mode((loadConfig.SCREEN_HEIGHT, loadConfig.SCREEN_WIDTH))
def main(screen):
    def start_the_game():
        mainGame.main(screen)

    def Skirmish():
        skirmishMenu.main(screen)

    def CreateMap():
        pass

    menu = pygame_menu.Menu(loadConfig.GAME_NAME, loadConfig.SCREEN_HEIGHT, loadConfig.SCREEN_WIDTH,
                           theme=pygame_menu.themes.THEME_DEFAULT)

    menu.add.clock(align=pygame_menu.locals.ALIGN_RIGHT)
    menu.add.vertical_margin(200)
    menu.add.button('Story', start_the_game)
    menu.add.button('Skirmish', Skirmish)
    menu.add.button('Create Map', CreateMap)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)


main(screen)