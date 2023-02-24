import turtle
from random import choices

# chips fallsen von oben nach unten
# chips haben zwei farben
# gibt es 4 chips in einer reihe gewinnt eine Farbe
# zwei spieler

space = 100
game_over = False
Turn = "yellow"
chip_liste = []

class chip:
    def __init__(self):
        self.body = turtle.Turtle()
        self.body.shape("circle")
        self.body.color(Turn)
        self.body.shapesize(4, 4)
        self.body.penup()
        self.body.goto(300, 300)
        self.colour = Turn
        chip_liste.append(self)

    def X(self):
        return int(self.body.xcor() / space) + 3

    def Y(self):
        return int(self.body.ycor() / space) + 3

    def POS(self):
        return (self.X(), self.Y())


def new_chip():
    Chip = chip()

class pseudo_chip:
    def __init__(self, pos):
        self.pos = pos
        self.colour = "red"
        self.EX = self.pos[0]
        self.EY = self.pos[1]

    def X(self):
        return self.EX

    def Y(self):
        return self.EY

    def POS(self):
        return (self.X(), self.Y())


wn = turtle.Screen()
wn.title("Shitty Vier Gewinnt")
wn.bgcolor("blue")
wn.setup(7 * space, 7 * space)
wn.tracer(0)

canvas = wn.getcanvas()

top = turtle.Turtle()
top.shape("square")
top.color("black")
top.shapesize(10, 70)
top.penup()
top.goto(0, 350)

lines_1 = turtle.Turtle()
lines_1.color("black")
lines_1.penup()
lines_1.setpos(space / 2, 7 * space + (space / 2))

lines_2 = turtle.Turtle()
lines_2.color("black")
lines_2.penup()
lines_2.setpos(-space / 2, 7 * space + (space / 2))

lines_3 = turtle.Turtle()
lines_3.color("black")
lines_3.penup()
lines_3.setpos(7 * space + (space / 2), (space / 2))

lines_4 = turtle.Turtle()
lines_4.color("black")
lines_4.penup()
lines_4.setpos(7 * space + (space / 2), -(space / 2))

lines_1.pendown()
lines_2.pendown()
lines_3.pendown()
lines_4.pendown()

for a in range(12):
    if lines_1.ycor() > 0:
        lines_1.sety(- 8 * space)
    else:
        lines_1.sety(8 * space)
    lines_1.setx((space / 2) + a * space)
    if lines_2.ycor() > 0:
        lines_2.sety(-8 * space)
    else:
        lines_2.sety(8 * space)
    lines_2.setx((space / 2) - a * space)
    if lines_3.xcor() > 0:
        lines_3.setx(-10 * space)
    else:
        lines_3.setx(10 * space)
    lines_3.sety((space / 2) + a * space)
    if lines_4.xcor() > 0:
        lines_4.setx(-10 * space)
    else:
        lines_4.setx(10 * space)
    lines_4.sety((space / 2) - a * space)

raster_liste = []

for x in range(0, 42):
    hole = turtle.Turtle()
    hole.shape("circle")
    hole.color("black")
    hole.shapesize(4, 4)
    hole.penup()
    raster_liste.append(hole)
    if x < 7:
        raster_liste[x].goto(-300 + (x * 100), 200)
    elif x < 14:
        raster_liste[x].goto(-300 + ((x - 7) * 100), 100)
    elif x < 21:
        raster_liste[x].goto(-300 + ((x - 14) * 100), 0)
    elif x < 28:
        raster_liste[x].goto(-300 + ((x - 21) * 100), -100)
    elif x < 35:
        raster_liste[x].goto(-300 + ((x - 28) * 100), -200)
    else:
        raster_liste[x].goto(-300 + ((x - 35) * 100), -300)

new_chip()


def bewegenrechts():
    if game_over == False:
        if Turn == "yellow":
            if chip_liste[-1].body.xcor() < 201:
                x = chip_liste[-1].body.xcor()
                x = x + space
                chip_liste[-1].body.setx(x)
            else:
                chip_liste[-1].body.setx(-300)
        else:
            if chip_liste[-1].body.xcor() < 201:
                x = chip_liste[-1].body.xcor()
                x = x + space
                chip_liste[-1].body.setx(x)
            else:
                chip_liste[-1].body.setx(-300)
    else:
        pass


def bewegenlinks():
    if game_over == False:
        if Turn == "yellow":
            if chip_liste[-1].body.xcor() > -201:
                x = chip_liste[-1].body.xcor()
                x = x - space
                chip_liste[-1].body.setx(x)
            else:
                chip_liste[-1].body.setx(300)
        else:
            if chip_liste[-1].body.xcor() > -201:
                x = chip_liste[-1].body.xcor()
                x = x - space
                chip_liste[-1].body.setx(x)
            else:
                chip_liste[-1].body.setx(300)
    else:
        pass


def Win(Liste):
    win = False
    for First in Liste:
        for Second in Liste:
            if First.X() == Second.X() + 1 and First.colour == Second.colour and First.Y() == Second.Y():
                for Third in Liste:
                    if First.X() == Third.X() + 2 and First.colour == Third.colour and First.Y() == Third.Y():
                        for Fourth in Liste:
                            if First.X() == Fourth.X() + 3 and First.colour == Fourth.colour and First.Y() == Fourth.Y() and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                print(First.POS(), Second.POS(), Third.POS(), Fourth.POS())
    for First in Liste:
        for Second in Liste:
            if First.Y() == Second.Y() + 1 and First.colour == Second.colour and First.X() == Second.X():
                for Third in Liste:
                    if First.Y() == Third.Y() + 2 and First.colour == Third.colour and First.X() == Third.X():
                        for Fourth in Liste:
                            if First.Y() == Fourth.Y() + 3 and First.colour == Fourth.colour and First.X() == Fourth.X() and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                print(First.POS(), Second.POS(), Third.POS(), Fourth.POS())
    for First in Liste:
        for Second in Liste:
            if First.Y() == Second.Y() + 1 and First.X() == Second.X() + 1 and First.colour == Second.colour:
                for Third in Liste:
                    if First.Y() == Third.Y() + 2 and First.X() == Third.X() + 2 and First.colour == Third.colour:
                        for Fourth in Liste:
                            if First.Y() == Fourth.Y() + 3 and First.X() == Fourth.X() + 3 and First.colour == Fourth.colour and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                print(First.POS(), Second.POS(), Third.POS(), Fourth.POS())
    for First in Liste:
        for Second in Liste:
            if First.Y() == Second.Y() + 1 and First.X() == Second.X() - 1 and First.colour == Second.colour:
                for Third in Liste:
                    if First.Y() == Third.Y() + 2 and First.X() == Third.X() - 2 and First.colour == Third.colour:
                        for Fourth in Liste:
                            if First.Y() == Fourth.Y() + 3 and First.X() == Fourth.X() - 3 and First.colour == Fourth.colour and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                print(First.POS(), Second.POS(), Third.POS(), Fourth.POS())

    if win == True:
        return True
    else:
        return False


def RedWin(Liste):
    win = False
    for First in Liste:
        for Second in Liste:
            if First.X() == Second.X() + 1 and First.colour == "red" and Second.colour == "red" and First.Y() == Second.Y():
                for Third in Liste:
                    if First.X() == Third.X() + 2 and First.colour == Third.colour and First.Y() == Third.Y():
                        for Fourth in Liste:
                            if First.X() == Fourth.X() + 3 and First.colour == Fourth.colour and First.Y() == Fourth.Y() and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                # print("Red",First.POS(), Second.POS(), Third.POS(), Fourth.POS())
    for First in Liste:
        for Second in Liste:
            if First.Y() == Second.Y() + 1 and First.colour == "red" and Second.colour == "red" and First.X() == Second.X():
                for Third in Liste:
                    if First.Y() == Third.Y() + 2 and First.colour == Third.colour and First.X() == Third.X():
                        for Fourth in Liste:
                            if First.Y() == Fourth.Y() + 3 and First.colour == Fourth.colour and First.X() == Fourth.X() and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                # print("Red",First.POS(), Second.POS(), Third.POS(), Fourth.POS())
    for First in Liste:
        for Second in Liste:
            if First.Y() == Second.Y() + 1 and First.X() == Second.X() + 1 and First.colour == "red" and Second.colour == "red":
                for Third in Liste:
                    if First.Y() == Third.Y() + 2 and First.X() == Third.X() + 2 and First.colour == Third.colour:
                        for Fourth in Liste:
                            if First.Y() == Fourth.Y() + 3 and First.X() == Fourth.X() + 3 and First.colour == Fourth.colour and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                # print("Red",First.POS(), Second.POS(), Third.POS(), Fourth.POS())
    for First in Liste:
        for Second in Liste:
            if First.Y() == Second.Y() + 1 and First.X() == Second.X() - 1 and First.colour == "red" and Second.colour == "red":
                for Third in Liste:
                    if First.Y() == Third.Y() + 2 and First.X() == Third.X() - 2 and First.colour == Third.colour:
                        for Fourth in Liste:
                            if First.Y() == Fourth.Y() + 3 and First.X() == Fourth.X() - 3 and First.colour == Fourth.colour and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                # print("Red",First.POS(), Second.POS(), Third.POS(), Fourth.POS())

    if win == True:
        return True
    else:
        return False


def YellowWin(Liste):
    win = False
    for First in Liste:
        for Second in Liste:
            if First.X() == Second.X() + 1 and First.colour == "yellow" and Second.colour == "yellow" and First.Y() == Second.Y():
                for Third in Liste:
                    if First.X() == Third.X() + 2 and First.colour == Third.colour and First.Y() == Third.Y():
                        for Fourth in Liste:
                            if First.X() == Fourth.X() + 3 and First.colour == Fourth.colour and First.Y() == Fourth.Y() and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                # print("Yellow",First.POS(), Second.POS(), Third.POS(), Fourth.POS())
    for First in Liste:
        for Second in Liste:
            if First.Y() == Second.Y() + 1 and First.colour == "yellow" and Second.colour == "yellow" and First.X() == Second.X():
                for Third in Liste:
                    if First.Y() == Third.Y() + 2 and First.colour == Third.colour and First.X() == Third.X():
                        for Fourth in Liste:
                            if First.Y() == Fourth.Y() + 3 and First.colour == Fourth.colour and First.X() == Fourth.X() and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                # print("Yellow",First.POS(), Second.POS(), Third.POS(), Fourth.POS())
    for First in Liste:
        for Second in Liste:
            if First.Y() == Second.Y() + 1 and First.X() == Second.X() + 1 and First.colour == "yellow" and Second.colour == "yellow":
                for Third in Liste:
                    if First.Y() == Third.Y() + 2 and First.X() == Third.X() + 2 and First.colour == Third.colour:
                        for Fourth in Liste:
                            if First.Y() == Fourth.Y() + 3 and First.X() == Fourth.X() + 3 and First.colour == Fourth.colour and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                # print("Yellow",First.POS(), Second.POS(), Third.POS(), Fourth.POS())
    for First in Liste:
        for Second in Liste:
            if First.Y() == Second.Y() + 1 and First.X() == Second.X() - 1 and First.colour == "yellow" and Second.colour == "yellow":
                for Third in Liste:
                    if First.Y() == Third.Y() + 2 and First.X() == Third.X() - 2 and First.colour == Third.colour:
                        for Fourth in Liste:
                            if First.Y() == Fourth.Y() + 3 and First.X() == Fourth.X() - 3 and First.colour == Fourth.colour and First.POS() != (
                            6, 6) and Fourth.POS() != (6, 6):
                                win = True
                                # print("Yellow",First.POS(), Second.POS(), Third.POS(), Fourth.POS())

    if win == True:
        return True
    else:
        return False


leereliste = []


def gameover():
    global game_over
    text = turtle.Turtle()
    text.speed(1)
    text.shape("square")
    text.color("red")
    text.shapesize(stretch_wid=2, stretch_len=2)
    text.penup()
    text.goto(-200, 265)
    text.hideturtle()
    for x in raster_liste:
        x.hideturtle()
    for x in chip_liste:
        x.body.hideturtle()
    text.write("GAME OVER {} wins".format(Turn), align="center", font=("Arial", 72, "bold"))
    leereliste.append(text)
    game_over = True


row = [0, 0, 0, 0, 0, 0, 0]


def Enterchip():
    global Turn
    chip_set = True
    if row[chip_liste[-1].X()] == 0:
        chip_liste[-1].body.sety(-300)
        row[chip_liste[-1].X()] = 1
    elif row[chip_liste[-1].X()] == 1:
        chip_liste[-1].body.sety(-200)
        row[chip_liste[-1].X()] = 2
    elif row[chip_liste[-1].X()] == 2:
        chip_liste[-1].body.sety(-100)
        row[chip_liste[-1].X()] = 3
    elif row[chip_liste[-1].X()] == 3:
        chip_liste[-1].body.sety(0)
        row[chip_liste[-1].X()] = 4
    elif row[chip_liste[-1].X()] == 4:
        chip_liste[-1].body.sety(100)
        row[chip_liste[-1].X()] = 5
    elif row[chip_liste[-1].X()] == 5:
        chip_liste[-1].body.sety(200)
        row[chip_liste[-1].X()] = 6
    else:
        chip_set = False

    if chip_set == False or game_over == True:
        pass
    else:
        if Win(chip_liste) == True:
            gameover()
        else:
            if Turn == "yellow":
                Turn = "red"
                new_chip()
                wn.update()
                cpu_action()
            else:
                Turn = "yellow"
                new_chip()


def Exit():
    global flag
    flag = False


loading_block_0 = turtle.Turtle()
loading_block_0.shape("circle")
loading_block_0.color("white")
loading_block_0.shapesize(3, 3)
loading_block_0.penup()
loading_block_0.goto(-200, 300)
loading_block_0.hideturtle()

loading_block_1 = turtle.Turtle()
loading_block_1.shape("circle")
loading_block_1.color("white")
loading_block_1.shapesize(3, 3)
loading_block_1.penup()
loading_block_1.goto(-100, 300)
loading_block_1.hideturtle()

loading_block_2 = turtle.Turtle()
loading_block_2.shape("circle")
loading_block_2.color("white")
loading_block_2.shapesize(3, 3)
loading_block_2.penup()
loading_block_2.goto(0, 300)
loading_block_2.hideturtle()

loading_block_3 = turtle.Turtle()
loading_block_3.shape("circle")
loading_block_3.color("white")
loading_block_3.shapesize(3, 3)
loading_block_3.penup()
loading_block_3.goto(100, 300)
loading_block_3.hideturtle()

count = 0


def loading():
    global count
    if count >= 1:
        loading_block_0.showturtle()
    if count >= 3:
        loading_block_1.showturtle()
    if count >= 5:
        loading_block_2.showturtle()
    if count >= 7:
        loading_block_3.showturtle()


def cpu_action_1():
    bewegenrechts()
    Enterchip()


def cpu_action_2():
    bewegenrechts()
    bewegenrechts()
    Enterchip()


def cpu_action_3():
    bewegenrechts()
    bewegenrechts()
    bewegenrechts()
    Enterchip()


def cpu_action_4():
    bewegenlinks()
    bewegenlinks()
    bewegenlinks()
    Enterchip()


def cpu_action_5():
    bewegenlinks()
    bewegenlinks()
    Enterchip()


def cpu_action_6():
    bewegenlinks()
    Enterchip()


def cpu_action_7():
    Enterchip()


def insert_pseudo(EX, Liste):
    EY = 0
    for a in range(0, len(Liste) - 1):
        if Liste[a].X() == EX:
            if Liste[a].Y() == 5:
                EY = 6
            elif Liste[a].Y() == 4:
                EY = 5
            elif Liste[a].Y() == 3:
                EY = 4
            elif Liste[a].Y() == 2:
                EY = 3
            elif Liste[a].Y() == 1:
                EY = 2
            elif Liste[a].Y() == 0:
                EY = 1
    return (EX, EY)


def create_pseudolisten(Liste, color):
    pseudo_liste_0 = Liste.copy()
    pseudo_chip_0 = pseudo_chip(insert_pseudo(0, pseudo_liste_0))
    pseudo_liste_0.insert(-2, pseudo_chip_0)

    pseudo_liste_1 = Liste.copy()
    pseudo_chip_1 = pseudo_chip(insert_pseudo(1, pseudo_liste_1))
    pseudo_liste_1.insert(-2, pseudo_chip_1)

    pseudo_liste_2 = Liste.copy()
    pseudo_chip_2 = pseudo_chip(insert_pseudo(2, pseudo_liste_2))
    pseudo_liste_2.insert(-2, pseudo_chip_2)

    pseudo_liste_3 = Liste.copy()
    pseudo_chip_3 = pseudo_chip(insert_pseudo(3, pseudo_liste_3))
    pseudo_liste_3.insert(-2, pseudo_chip_3)

    pseudo_liste_4 = Liste.copy()
    pseudo_chip_4 = pseudo_chip(insert_pseudo(4, pseudo_liste_4))
    pseudo_liste_4.insert(-2, pseudo_chip_4)

    pseudo_liste_5 = Liste.copy()
    pseudo_chip_5 = pseudo_chip(insert_pseudo(5, pseudo_liste_5))
    pseudo_liste_5.insert(-2, pseudo_chip_5)

    pseudo_liste_6 = Liste.copy()
    pseudo_chip_6 = pseudo_chip(insert_pseudo(6, pseudo_liste_6))
    pseudo_liste_6.insert(-2, pseudo_chip_6)

    if color == "yellow":
        pseudo_chip_0.colour = "yellow"
        pseudo_chip_1.colour = "yellow"
        pseudo_chip_2.colour = "yellow"
        pseudo_chip_3.colour = "yellow"
        pseudo_chip_4.colour = "yellow"
        pseudo_chip_5.colour = "yellow"
        pseudo_chip_6.colour = "yellow"
    elif color == "red":
        pseudo_chip_0.colour = "red"
        pseudo_chip_1.colour = "red"
        pseudo_chip_2.colour = "red"
        pseudo_chip_3.colour = "red"
        pseudo_chip_4.colour = "red"
        pseudo_chip_5.colour = "red"
        pseudo_chip_6.colour = "red"
    else:
        pseudo_chip_0.colour = "white"
        pseudo_chip_1.colour = "white"
        pseudo_chip_2.colour = "white"
        pseudo_chip_3.colour = "white"
        pseudo_chip_4.colour = "white"
        pseudo_chip_5.colour = "white"
        pseudo_chip_6.colour = "white"

    return [pseudo_liste_0, pseudo_liste_1, pseudo_liste_2, pseudo_liste_3, pseudo_liste_4, pseudo_liste_5,
            pseudo_liste_6]



def cpu_action():
    global count
    wht = [1, 1, 1, 1, 1, 1, 1]
    actionliste = [cpu_action_1, cpu_action_2, cpu_action_3, cpu_action_4, cpu_action_5, cpu_action_6, cpu_action_7]

    pseudo_listen_first_red = create_pseudolisten(chip_liste, "red")
    pseudo_listen_first_yellow = create_pseudolisten(chip_liste, "yellow")

    for N in range(0, len(pseudo_listen_first_red)):
        if RedWin(pseudo_listen_first_red[N]) == True:
            wht[N] = wht[N] + 900000
            print("I Win. Row: {}".format(N + 1))

    for N in range(0, len(pseudo_listen_first_yellow)):
        if YellowWin(pseudo_listen_first_yellow[N]) == True:
            wht[N] = wht[N] + 9000
            print("You won`t win! Row: {}".format(N + 1))

    for U in range(0, len(pseudo_listen_first_red)):
        pseudo_listen_second_yellow = create_pseudolisten(pseudo_listen_first_red[U], "yellow")
        for N in range(0, len(pseudo_listen_second_yellow)):
            if YellowWin(pseudo_listen_second_yellow[N]) == True:
                wht[U] = wht[U] - 50
                # print("I will not give you this win. Row:{}".format(U))
                # for b in pseudo_listen_second_yellow:
                # print("-"*50)
                # for c in b:
                # print(c.POS(), c.colour)
    for T in range(0, len(pseudo_listen_first_red)):
        pseudo_listen_second_yellow = create_pseudolisten(pseudo_listen_first_red[T], "yellow")
        for U in range(0, len(pseudo_listen_second_yellow)):
            pseudo_listen_third_red = create_pseudolisten(pseudo_listen_second_yellow[U], "red")
            for N in range(0, len(pseudo_listen_third_red)):
                if RedWin(pseudo_listen_third_red[N]) == True:
                    wht[T] = wht[T] + 10
                    # print("I will win next turn Row:{}".format(T))
                    # for b in pseudo_listen_third_red:
                    # print("-"*50)
                    # for c in b:
                    # print(c.POS(), c.colour)

    for T in range(0, len(pseudo_listen_first_red)):
        pseudo_listen_second_yellow = create_pseudolisten(pseudo_listen_first_red[T], "yellow")
        for U in range(0, len(pseudo_listen_second_yellow)):
            pseudo_listen_third_red = create_pseudolisten(pseudo_listen_second_yellow[U], "red")
            for N in range(0, len(pseudo_listen_third_red)):
                pseudo_listen_fourth_yellow = create_pseudolisten(pseudo_listen_third_red[N], "yellow")
                for J in range(0, len(pseudo_listen_fourth_yellow)):
                    if YellowWin(pseudo_listen_fourth_yellow[J]) == True:
                        wht[T] = wht[T] - 10
                        # print("I will not give you the win next turn Row:{}".format(T))
                        # for b in pseudo_listen_third_red:
                        # print("-"*50)
                        # for c in b:
                        # print(c.POS(), c.colour)

    count = 0
    for T in range(0, len(pseudo_listen_first_red)):
        pseudo_listen_second_yellow = create_pseudolisten(pseudo_listen_first_red[T], "yellow")
        count += 1
        loading()
        wn.update()
        for U in range(0, len(pseudo_listen_second_yellow)):
            pseudo_listen_third_red = create_pseudolisten(pseudo_listen_second_yellow[U], "red")
            for N in range(0, len(pseudo_listen_third_red)):
                pseudo_listen_fourth_yellow = create_pseudolisten(pseudo_listen_third_red[N], "yellow")
                for J in range(0, len(pseudo_listen_fourth_yellow)):
                    pseudo_listen_fifth_red = create_pseudolisten(pseudo_listen_fourth_yellow[J], "red")
                    for L in range(0, len(pseudo_listen_fifth_red)):
                        if RedWin(pseudo_listen_fifth_red[L]) == True:
                            wht[T] = wht[T] + 1
                            # print("I will not give you the win next turn Row:{}".format(T))
                            # for b in pseudo_listen_third_red:
                            # print("-"*50)
                            # for c in b:
                            # print(c.POS(), c.colour)

    for x in range(0, len(row)):
        if row[x] == 6:
            wht[x] = 0
        if wht[x] < 0:
            wht[x] = 0
    if wht == [0, 0, 0, 0, 0, 0, 0]:
        wht = [11, 11, 11, 11, 11, 11, 11]
        for x in range(0, len(row)):
            if row[x] == 6:
                wht[x] = 0
    if wht != [11, 11, 11, 11, 11, 11, 11]:
        print(wht)
    else:
        print("I don't know what to do...")
    act = choices(actionliste, wht)
    act[0]()
    loading_block_0.hideturtle()
    loading_block_1.hideturtle()
    loading_block_2.hideturtle()
    loading_block_3.hideturtle()


def Eikesidee():
    if chip_liste[-2].Y() == 6:
        row[chip_liste[-2].X()] = 5
    elif chip_liste[-2].Y() == 5:
        row[chip_liste[-2].X()] = 4
    elif chip_liste[-2].Y() == 4:
        row[chip_liste[-2].X()] = 3
    elif chip_liste[-2].Y() == 3:
        row[chip_liste[-2].X()] = 2
    elif chip_liste[-2].Y() == 2:
        row[chip_liste[-2].X()] = 1
    else:
        row[chip_liste[-2].X()] = 0
    chip_liste[-2].body.hideturtle()
    chip_liste.pop(-2)

    if chip_liste[-2].Y() == 6:
        row[chip_liste[-2].X()] = 5
    elif chip_liste[-2].Y() == 5:
        row[chip_liste[-2].X()] = 4
    elif chip_liste[-2].Y() == 4:
        row[chip_liste[-2].X()] = 3
    elif chip_liste[-2].Y() == 3:
        row[chip_liste[-2].X()] = 2
    elif chip_liste[-2].Y() == 2:
        row[chip_liste[-2].X()] = 1
    else:
        row[chip_liste[-2].X()] = 0
    chip_liste[-2].body.hideturtle()
    chip_liste.pop(-2)


def Pass():
    pass


wn.listen()
wn.onkeypress(Exit, "h")
# if chip_liste[-1].colour == "yellow":
# wn.onkeypress(bewegenrechts, "Right")
# wn.onkeypress(bewegenlinks, "Left")
# wn.onkeypress(Enterchip, "Down")
# wn.onkeypress(Eikesidee, "g")
flag = True

while flag == True:
    if chip_liste[-1].colour == "yellow":
        wn.onkeypress(bewegenrechts, "Right")
        wn.onkeypress(bewegenlinks, "Left")
        wn.onkeypress(Enterchip, "Down")
        wn.onkeypress(Eikesidee, "g")
    else:
        wn.onkeypress(Pass, "Right")
        wn.onkeypress(Pass, "Left")
        wn.onkeypress(Pass, "Down")
        wn.onkeypress(Pass, "g")
    wn.update()
