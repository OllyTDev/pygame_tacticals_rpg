import pygame
import mainGame
import maps
from classes import Player, colour
from drawFunctions import column, row, drawButton, drawTable
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

def findCellClicked(pos):
    pass

def extractFromTable(rows):
    players = []
    for row in rows:
        if (row.data["Player"] != ""):
            newPlayer = Player(row.data["Player"], row.data["Colour"], row.data["Team"], row.data["Faction"])
            print("created:", newPlayer.name, "playing as ", newPlayer.faction, "on team ", newPlayer.team, "as colour : ", newPlayer.colour)
            players.append(newPlayer)
        else:
            print("Row empty, skipping.")
    print(len(players), "players created" )      
    return players      

def start(screen, rows):
    players = extractFromTable(rows)
    mainGame.main(screen, maps.sandMap, players)

def quit():
    global running
    running = False

def main(screen):

    screen.fill(colour.LightBlue)

    def intialTables():
        skirmishColumns = [column("Colour",("colour"),buffer_X=10), column("Player", buffer_X=75), column("Faction", buffer_X=75), column("Team", buffer_X=50)]
        
        tableEmptyValue = [("Colour",(colour.Black)), ("Player", ""), ("Faction", ""), ("Team", "") ]            
        dummyRow = row()
        dummyRow.addData(tableEmptyValue)

        values = [("Colour",(colour.Red)), ("Player", "Player1"), ("Faction", "Faction1"), ("Team", "team1") ]
        values2 = [("Colour",(colour.Blue)), ("Player", "Player2"), ("Faction", "Faction2"), ("Team", "team2") ]
        row1 = row()
        row1.addData(values)
        row2 = row()
        row2.addData(values2)
        
        rows = [row1, row2, dummyRow, dummyRow]

        buttons = drawTable(screen, skirmishColumns, rows, (25,150))
        pygame.display.update()
        return (rows, buttons)


    defaultButtonSize = [200, 35]
    startButton = drawButton(screen, "Start", (500, 500), size = defaultButtonSize)
    backButton = drawButton(screen, "Back",  (100, 500), size = defaultButtonSize)

    global players
    players = 2
    rowsAndRects = intialTables()
    rows = rowsAndRects[0]
    buttons = rowsAndRects[1]
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
                    start(screen, rows)    
                for b in buttons:
                    if b.collidepoint(pos):
                        print("found a button @", pos)
                        findCellClicked(pos)
                        #pos[0] (x value) -> tells us which player data we're changing
                        #pos[1] (y value) -> tells us which column you're changing
                        #display options, user selects option
                        #then updateTable()
                        print("Now can you tell me which button?")