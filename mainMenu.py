import pygame
import pygame_menu
import loadConfig
import skirmishMenu

pygame.init()

screen = pygame.display.set_mode((loadConfig.SCREEN_WIDTH, loadConfig.SCREEN_HEIGHT))
def main(screen):
    def storyMenu():
        print("Display the story menu!")

    def Skirmish():
        skirmishMenu.main(screen)

    def CreateMap():
        pass

    menu = pygame_menu.Menu(loadConfig.GAME_NAME, loadConfig.SCREEN_WIDTH, loadConfig.SCREEN_HEIGHT,
                           theme=pygame_menu.themes.THEME_DEFAULT)

    menu.add.clock(align=pygame_menu.locals.ALIGN_RIGHT)
    menu.add.vertical_margin(250)
    menu.add.button('Story', storyMenu)
    menu.add.button('Skirmish', Skirmish)
    menu.add.button('Create Map', CreateMap)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)


main(screen)