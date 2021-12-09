import pygame
import mainGame
import maps
import math
from classes import Player, colour
from UI_Classes import DropDown
from drawFunctions import column, row, drawButton, drawTable
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

def findCellClicked(cellNumber):
    columnClicked = ""
    rowClicked = ""

    if (cellNumber % 4 == 1):
        columnClicked = 1
    elif (cellNumber % 4 == 2):
        columnClicked = 2 
    elif (cellNumber % 4 == 3):
        columnClicked = 3
    elif (cellNumber % 4 == 0):
        columnClicked = 4

    if (math.ceil(cellNumber / 4) == 1):
        rowClicked = 1
    elif (math.ceil(cellNumber / 4) == 2):
        rowClicked = 2  
    elif (math.ceil(cellNumber / 4) == 3):
        rowClicked = 3
    elif (math.ceil(cellNumber / 4) == 4):
        rowClicked = 4   

    return (rowClicked, columnClicked)

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

def initialSkirmishUI(screen):
    screen.fill(colour.LightBlue)
    defaultButtonSize = [200, 35]
    drawButton(screen, "Start", (500, 500), size = defaultButtonSize)
    drawButton(screen, "Back",  (100, 500), size = defaultButtonSize)
    pygame.display.flip()

def setDropDownText(buttonColumn):
    if (buttonColumn == 2):
        return "Player"
    elif (buttonColumn == 3):
        return "Faction"
    elif (buttonColumn == 4):
        return "Team"
    else:
        return ""    

def setDropDownOptions(buttonColumn):
    if (buttonColumn == 2):
        return ["Player 1", "Player 2", "Player 3", "Player 4"]
    elif (buttonColumn == 3):
        return ["Warriors", "Thieves", "Mages"]
    elif (buttonColumn == 4):
        return ["Team 1", "Team 2", "Team 3", "Team 4"]
    else:
        return ["",""]

def createDropdowns(buttons):
    ddList = []
    i = 0
    for b in buttons:
        i = i + 1
        buttonColumn = findCellClicked(i)[1]

        Text = setDropDownText(buttonColumn)
        Options = setDropDownOptions(buttonColumn)
        
        if (buttonColumn != 1):
            dd = DropDown(
                [colour.White, colour.SelectionBlue],
                [colour.White, colour.SelectionBlue],
                b.x+1, b.y+1, b.w-2, b.h-2, 
                pygame.font.SysFont("Arial", 25), 
                Text, Options, i)  
            ddList.append(dd)
    return ddList    
    
def updateDropdown(screen, intialTables, dropDown, event_list):
    selected_option = dropDown.update(event_list)
    if selected_option >= 0:
        initialSkirmishUI(screen)  
        intialTables()
        dropDown.main = dropDown.options[selected_option]  
        dropDown.draw(screen)      
    
def main(screen):

    screen.fill(colour.LightBlue)

    def updateTables(rows):
        skirmishColumns = [column("Colour",("colour"),buffer_X=10), column("Player", buffer_X=75), column("Faction", buffer_X=75), column("Team", buffer_X=50)]

        tableEmptyValue = [("Colour",(colour.Black)), ("Player", ""), ("Faction", ""), ("Team", "") ]            
        dummyRow = row()
        dummyRow.addData(tableEmptyValue)

        buttons = drawTable(screen, skirmishColumns, rows, (25,150))
        pygame.display.flip()
        return (rows, buttons)


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
        pygame.display.flip()
        return (rows, buttons)


    defaultButtonSize = [200, 35]
    startButton = drawButton(screen, "Start", (500, 500), size = defaultButtonSize)
    backButton = drawButton(screen, "Back",  (100, 500), size = defaultButtonSize)  


    global players
    players = 2
    rowsAndRects = intialTables()
    rows = rowsAndRects[0]
    tableRects = rowsAndRects[1]

    dropDownList = createDropdowns(tableRects)
    pygame.display.update()

    clock = pygame.time.Clock()
    global running
    running = True
    dropdownClicked = 0

    while running:
        clock.tick(10)
        event_list = pygame.event.get()
        for event in event_list:
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
                i = 0      
                for b in tableRects:
                    i = i + 1
                    if b.collidepoint(pos):
                        buttonClicked = findCellClicked(i)
                        print(buttonClicked)
                        if (buttonClicked[1] != 1):
                            for dd in dropDownList:
                                if (dd.buttonNumber == i):
                                    dropdownClicked = dd

        if (dropdownClicked != 0):
            selected_option = dropdownClicked.update(event_list)
            if selected_option >= 0:
                dropdownClicked.main = dropdownClicked.options[selected_option] 
        
        if (dropdownClicked != 0):
            initialSkirmishUI(screen)  
            intialTables()
            dropdownClicked.draw(screen)
        pygame.display.flip() 
                