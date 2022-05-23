# 使用turtle库的turtle.circle()函数，turtle.seth()函数，turtle.left()函数绘制一个四瓣花图案，效果如图所示。
from turtle import *
speed(0)
pu()
fd(150)
seth(90)
fd(150)
for i in range(3):
    pd()
    circle(150, -180)
    pu()
    fd(300)
    left(90)
    pd()
    circle(150, 180)
ht()
done()
