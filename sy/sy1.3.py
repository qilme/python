from turtle import *
from random import *
colormode(255)
speed(0)
R = 200
right(90)
for i in range(9):
    r, g, b = randint(1, 255), randint(1, 255), randint(1, 255)
    pencolor(r, g, b)
    fillcolor(r, g, b)
    R -= 20
    pu()
    goto(-R, 0)
    pd()
    begin_fill()
    circle(R, 360)
    end_fill()
ht()
done()
