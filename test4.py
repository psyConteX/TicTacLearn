import turtle
space = 100
wn = turtle.Screen()
wn.title("Shitty Vier Gewinnt")
wn.bgcolor(0,0,0)
wn.setup(7 * space, 7 * space)
wn.tracer(1)
# print(x,y)
turtle.showturtle
turtle.shape("turtle")
turtle.shapesize = 1000
turtle.setposition(wn.canvwidth/2,wn.canvheight/2)
turtle.home
turtle.pencolor(1,1,1)
y=0
turtle.speed=2
while (y<2000):
    print(y)
    turtle.forward(1)
    turtle.right(1)
    y+=1
    if y % 270 == 0:
        turtle.left(90)
    if y == 270*2+230:
        break
turtle.left(90)
# turtle.right(180)
for i in range(200):
    turtle.forward(1)
turtle.left(90)

for i in range(150):
    turtle.forward(2)
    if i <50 or i>100:
        turtle.right(3)
    else: 
        turtle.right(1)   
turtle.left(80)
for i in range(190):
    turtle.forward(1)







input()