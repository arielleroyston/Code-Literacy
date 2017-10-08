from turtle import *

screensize(2000,1500) #define x,y coordinates
hideturtle() # hide turtle
fillcolor('red')  # make red heart
pencolor('red') # make red line
bgcolor('navy')
speed(0)

# define curve of hearts
def curvemove():
    for i in range(100):
        right(2)
        forward(1)

# define heart shape
def heart():
    begin_fill()
    left(140)
    forward(60)
    curvemove()
    left(120)
    curvemove()
    left(2)
    forward(56)
    end_fill()

# define a row of hearts
def drawRow():
    for i in range(6):
        pendown()
        heart()
        penup()
        setheading(0)
        forward(120)

# draw first row at bottom left
# stack 6 rows
for i in range(6):
    penup()
    goto(-440, -500 + i * 120)
    drawRow()
