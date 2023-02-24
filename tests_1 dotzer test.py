def isfloat(string):
    if string == "" or string == ".":
        return False
    count = 0
    for x in range(0, len(string)):
        if string[x].isdigit():
            pass
        elif string[x] == ".":
            count += 1
        else:
            return False
    if count <= 1:
        return True
    else:
        return False


def add():
    zahl1 = input("Gib bitte eine Zahl ein.")
    zahl2 = input("Gib bitte eine weitere Zahl ein")

    if not isfloat(zahl1) or not isfloat(zahl2):
        print("Bitte gib dir mehr mühe")
        add()
    else:
        print(float(zahl1) + float(zahl2))


# add()


def invert(string):
    """Invert a given string"""
    # declare the new string
    new_string = ""
    # looping through every string index, tearing the string apart
    for string_index in range(0, len(string)):
        # putting the new inverted string together
        new_string = string[string_index] + new_string

    return new_string


# TicTacToe

row_2 = [" ", " ", " "]
row_1 = [" ", " ", " "]
row_0 = [" ", " ", " "]

board = [row_0, row_1, row_2]

turn = "O"
flag = True


def action():
    global flag
    print()
    print(f"Player '{turn}': make a move!")
    print()
    a = input("Row:")
    if a == "Exit":
        flag = False
        return None
    if a == "1" or a == "2" or a == "3":
        b = input("Column:")
        if b == "Exit":
            flag = False
            return None
        print()
        if b == "1" or b == "2" or b == "3":
            a = int(a)
            b = int(b) - 1
            if board[-a][b] == " ":
                board[-a][b] = turn
            else:
                print("Invalid! Field already occupied")
                print()
                action()
        else:
            print("Invalid input")
            print()
            action()
    else:
        print("Invalid input")
        print()
        action()


def new_turn():
    if turn == "O":
        return "X"
    else:
        return "O"


def game_over():
    for row in board:
        if row[0] != " " and row[0] == row[1] and row[0] == row[2]:
            print()
            print(f"Player {turn} won!")
            return True

    if board[0][0] != " " and board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        print()
        print(f"Player {turn} won!")
        return True
    if board[0][1] != " " and board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        print()
        print(f"Player {turn} won!")
        return True
    if board[0][2] != " " and board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        print()
        print(f"Player {turn} won!")
        return True

    if board[0][0] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        print()
        print(f"Player {turn} won!")
        return True
    if board[2][0] != " " and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        print()
        print(f"Player {turn} won!")
        return True

    count = 0
    for row in board:
        for position in row:
            if position != " ":
                count += 1
    if count == 9:
        print()
        print("Draw!")
        return True

    return False


def print_board():
    print("  1   2   3")
    print(f"1 {row_2[0]} | {row_2[1]} | {row_2[2]}")
    print(f"2 {row_1[0]} | {row_1[1]} | {row_1[2]}")
    print(f"3 {row_0[0]} | {row_0[1]} | {row_0[2]}")


# Programmstart:

print()
print("Tic Tac Toe; Type 'Exit' to close")
print()
print_board()

while flag:
    action()
    print_board()
    if game_over():
        flag = False
    turn = new_turn()

