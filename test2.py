from random import randint, random, randrange


c = 3
r = 3
#x = [ [0] * c for i in range(r) ] old stuff
#y = [ [0] * c for i in range(r) ]
taken = [ [0] * c for i in range(r) ]
turn = 1
turnCounter = 0
global gameStart
gameStart = True
ki_an = False

def checkwin(player):#checks if active player wins
    global gameStart
    for i in range(0,c): # Counting "player" in colum
        points = 0
        for ii in range(0,r):
            if taken[i][ii] == player:
                points += 1
                if points >= 3:
                    updateWIN(player)
                    gameStart = False
    for ii in range(0,c): #  Counting "player" in ROW
        points = 0
        for i in range(0,r):
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
def playermove(turn):#changes the turn order
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
def clearscreen():#"clears" the terminal
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def Set(player):#sets the players symbol
    if ki_an == True:
        if turn == 1:
            KeyInput=input()
            if KeyInput.isdigit():
                keyCheck(KeyInput, player)
            else:
                print("Wrong Input")
                Set(player)

        else:
            KeyInput=randint(0,9) #massive KI
            keyCheck(KeyInput, player)
    else: 
        KeyInput=input()
        keyCheck(KeyInput, player)
def printBoard():#prints the board on call
    iii=0
    print("----------")
    for i in range(0,r):
        for ii in range(0,c):
                iii+=1
                if taken[i][ii]!='x' and taken[i][ii]!='y':
                    taken[i][ii]=iii
        print(taken[i][0],'|',taken[i][1],'|',taken[i][2])
        print("----------")
def updateWIN(player):#reset screen when a player wins and prints the final set
    clearscreen()
    printBoard()
    print(player, "wins")
def keyCheck(KeyInput, player):#checking a int
    global taken
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


while gameStart:
    clearscreen()
    printBoard()
    if turnCounter >= 9: #if after 9 turns there is no winner its a draw
        gameStart = False
        print("Draw")
    if gameStart == True:#if the game is running let a player make a move
        turn = playermove(turn)
    checkwin('x')     
    checkwin('y')        
#playerturns