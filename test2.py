from turtle import update


c = 3
r = 3
#x = [ [0] * c for i in range(r) ]
#y = [ [0] * c for i in range(r) ]
taken = [ [0] * c for i in range(r) ]
turn = 1
turnCounter = 0
global gameStart
gameStart = True
gameWin='O'

def checkwin(player):
    global gameStart
    for i in range(0,3): # Counting "player" in colum
        points = 0
        for ii in range(0,3):
            if taken[i][ii] == player:
                points += 1
                if points >= 3:
                    updateWIN(player)
                    gameStart = False
    for ii in range(0,3): #  Counting "player" in ROW
        points = 0
        for i in range(0,3):
            if taken[i][ii] == player:
                points += 1
                if points >= 3:
                    updateWIN(player)
                    gameStart = False
    if taken[0][0] == player and taken[1][1] == player and taken[2][2] == player: # WIN condition top left middle bottom right
        updateWIN(player)
        gameStart = False
    if taken[0][2] == player and taken[1][1] == player and taken[2][0] == player: # WIN condition top right middle bottom left
        gameStart = False        
        updateWIN(player)
    return True
def playermove(turn):
    if (turn==1):
        turn = turn *-1
        print("x's turn")
        Set('x')
        return turn
    else:
        turn = turn *-1
        print("y's turn")
        Set('y')
        return turn
def clearscreen():
    print("""
    
    
    
    
    
    






    
    """)
def Set(player):
    KeyInput=input()
    if KeyInput.isdigit():
        if int(KeyInput) >=1 and int(KeyInput) <= 9:
            if taken[(int(KeyInput)-1)//3][(int(KeyInput)-1)%3] != 'x' and taken[(int(KeyInput)-1)//3][(int(KeyInput)-1)%3]!= 'y':
                taken[(int(KeyInput)-1)//3][(int(KeyInput)-1)%3]=player
                global turnCounter
                turnCounter += 1
            else:
                print("Wrong Input")
                Set(player)
        else:
            print("Wrong Input")
            Set(player)    
    else:
        print("Wrong Input")
        Set(player)
def printBoard():
    iii=0
    print("----------")
    for i in range(0,3):
        for ii in range(0,3):
            if taken[i][ii]=='x':
                iii+=1
                pass
            elif taken[i][ii]=='y':
                iii+=1
                pass
            else:
                iii+=1
                taken[i][ii]=iii
        print(taken[i][0],'|',taken[i][1],'|',taken[i][2])
        print("----------")
def updateWIN(player):
    clearscreen()
    printBoard()
    print(player, "wins")
#         iii+=1
#         x[i][ii]='x'
#         y[i][ii]='y'
#         taken[i][ii]='O'

while gameStart:

    clearscreen()
    printBoard()
    if turnCounter >= 9:
        gameStart = False
        print("Draw")
    if gameStart == True:        
        turn = playermove(turn)
    checkwin('x')     
    checkwin('y')        
#playerturns