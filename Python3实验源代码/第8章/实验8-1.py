from turtle import *
import math
fc=['yellow','red','green','blue']#准备填充颜色
r=50
y=math.sqrt(4*r*r-r*r)
xy=[(r,0),(-r,0),(0,y),(0,-y)]#准备圆心
speed(2)                        #速度为0时，没有画图的动画过程
for i in range(4):              #绘制4个圆
    fillcolor(fc[i])
    pencolor(fc[i])
    up()
    goto(xy[i][0],xy[i][1]-r)
    pd()
    begin_fill()
    circle(r)
    end_fill()
#绘制坐标系
home()
pencolor('black')
goto(-3*r,0)
goto(3*r,0)
stamp()
up()
goto(3*r-20,10)
write('X')
goto(0,-3.5*r)
pd()
goto(0,3.5*r)
rt(90)
setheading(90)
stamp()
up()
goto(10,3.5*r-20)
write('Y')
goto(5,-20)
write("(0,0)")
ht()
