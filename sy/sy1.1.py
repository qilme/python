from turtle import *
import math

fc = ['yellow', 'red', 'green', 'blue']
r = 100
y = math.sqrt(4 * r * r - r * r)
xy = [(r, 0), (-r, 0), (0, y), (0, -y)]
speed(0)
for i in range(4):
    fillcolor(fc[i])
    pencolor(fc[i])
    up()
    goto(xy[i][0], xy[i][1] - r)
    pd()
    begin_fill()
    circle(r)
    end_fill()

home()
pencolor('black')
goto(-3 * r, 0)
goto(3 * r, 0)
stamp()
up()
goto(3 * r - 20, 10)
goto(0, -3.5 * r)
pd()
goto(0, 3.5 * r)
rt(90)
setheading(90)
stamp()
up()
goto(10, 3.5 * r - 20)
goto(5, -20)
ht()
done()
