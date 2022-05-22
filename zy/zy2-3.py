from turtle import *
# tracer(False)
p = Turtle()
b = Turtle()
p.speed(0), b.speed(0)
setup(650, 350, 200, 200)
p.penup()
p.fd(-250)
p.pendown()
p.pensize(25)
p.seth(-40)
co = ["blue", "green", "yellow", "orange"]
for i in range(4):
    p.pencolor(co[i])
    p.circle(40, 80)
    p.circle(-40, 80)
p.circle(40, 80/2)
p.fd(40)
p.circle(16, 180)
p.fd(40 * 2/3)
nu = 66  # eval(input("循环次数："))
ag, px = 90, 5
speed(0)
# pd()
for i in range(nu):
    b.lt(ag)
    b.fd(px)
    px += 5
done()
