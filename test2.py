c = 3
r = 3
x = [ [0] * c for i in range(r) ]
y = [ [0] * c for i in range(r) ]
taken = [ [0] * c for i in range(r) ]
turn = 1
gameStart=True
gameWin='O'
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
            else:
                print("Wrong Input")
                Set(player)
        else:
            print("Wrong Input")
            Set(player)    
    else:
        print("Wrong Input")
        Set(player)
def checkwin(player):
    for i in range(0,3):
        points = 0
        for ii in range(0,3):
            if taken[i][ii] == player:
                points += 1
                if points >= 3:
                    print(player, "wins")
                    return False
    for ii in range(0,3):
        points = 0
        for i in range(0,3):
            if taken[i][ii] == player:
                points += 1
                if points >= 3:
                    print(player, "wins")
                    return False
    if taken[0][0] == player and taken[1][1] == player and taken[2][2]:
        print(player,"wins")
        return False
    if taken[0][2] == player and taken[1][1] == player and taken[2][0]:    
        print(player,"wins")
        return False
    return True
#         iii+=1
#         x[i][ii]='x'
#         y[i][ii]='y'
#         taken[i][ii]='O'

while gameStart:
    iii=0
    clearscreen()
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
    turn = playermove(turn)
    if checkwin('x')==True:
        gameStart = checkwin('y')
    else: 
        gameStart = False
#playerturns