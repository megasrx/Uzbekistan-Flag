import turtle
from turtle import *

setup(1000, 600)
bgcolor("black")
speed(1)


penup()
goto(-400, 265)
pendown()

color("#0072CE")
begin_fill()
forward(800)
right(90)
forward(160)
right(90)
forward(800)
end_fill()

color("#DA291C")
begin_fill()
right(180)
forward(800)
right(90)
forward(10)
right(90)
forward(800)
end_fill()

color("white")
begin_fill()
right(180)
forward(800)
right(90)
forward(160)
right(90)
forward(800)
end_fill()

color("#DA291C")
begin_fill()
right(180)
forward(800)
right(90)
forward(10)
right(90)
forward(800)
end_fill()

color("#43B02A")
begin_fill()
right(180)
forward(800)
right(90)
forward(160)
right(90)
forward(800)
end_fill()

color("white")
penup()
goto(-270, 245)
pendown()
begin_fill()
circle(60)
end_fill()

color("#0072CE")
penup()
goto(-255, 245)
pendown()
begin_fill()
circle(60)
end_fill()


penup()
goto(-230, 135)
pendown()
color("white")
begin_fill()

right(180)


def draw_star():
    begin_fill()
    for i in range(5):
        forward(15)
        right(144)
    end_fill()
    return


for i in range(5):
    penup()
    goto(-230 + i * 35, 135)
    pendown()
    draw_star()


for i in range(4):
    penup()
    goto(-195 + i * 35, 185)
    pendown()
    draw_star()

for i in range(3):
    penup()
    goto(-160 + i * 35, 235)
    pendown()
    draw_star()

hideturtle()

turtle.done()
