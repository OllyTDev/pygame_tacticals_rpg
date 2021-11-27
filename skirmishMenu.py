import pygame
import pygame_menu
import loadConfig
from mainGame import changeTurns
#import mainMenu

pygame.init()

def main(screen):

    pauseMenu = pygame_menu.Menu(loadConfig.GAME_NAME, loadConfig.SCREEN_HEIGHT, loadConfig.SCREEN_WIDTH,
                       theme=pygame_menu.themes.THEME_DEFAULT)

    def start_the_game():
        pass

    def change_table():
        players.get_value()
        pass

    def back_button():
        pauseMenu.disable()

    pauseMenu.add.clock(align=pygame_menu.locals.ALIGN_RIGHT)
    pauseMenu.add.button('Start', start_the_game, align=pygame_menu.locals.ALIGN_LEFT)
    players = pauseMenu.add.dropselect('Players',["2","3","4"], default=0, placeholder="Select a number of players", align=pygame_menu.locals.ALIGN_LEFT)
    pauseMenu.add.image('Asset\\refresh.png', 0, scale=[0.5,0.5])

    table = pauseMenu.add.table("tbl1",)
    widgets = [pauseMenu.add.label("Player"), pauseMenu.add.label("Colour"), pauseMenu.add.label("Race")]
    table.add_row(widgets)
    
    pauseMenu.add.button('Back', back_button, align=pygame_menu.locals.ALIGN_LEFT)
    
    pauseMenu.mainloop(screen)
        


