import turtle
import datetime


def skip(d):
    turtle.penup()
    turtle.forward(d)
    turtle.pendown()


def draw_clock():
    turtle.reset()
    for i in range(60):
        skip(160)
        if i % 5 == 0:
            turtle.pensize(7)
            turtle.forward(20)
            if i == 0:
                turtle.write(12, align='center', font=('Courier', 14, 'bold'))
            elif i == 25 or i == 30 or i == 35:
                skip(25)
                turtle.write(int(i / 5), align='center', font=('Courier', 14, 'bold'))
                skip(-25)
            else:
                turtle.write(int(i / 5), align='center', font=('Courier', 14, 'bold'))
            skip(-20)
        else:
            turtle.pensize(1)
            turtle.dot()
        skip(-160)
        turtle.right(6)


def get_week(t):
    week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return week[t.weekday()]


def create_hand(length, name):
    turtle.reset()
    skip(-length * 0.1)
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    turtle.end_poly()

    turtle.register_shape(name, turtle.get_poly())
    hand = turtle.Turtle()
    hand.shape(name)
    hand.shapesize(1, 1, 3)
    return hand


def run():
    t = datetime.datetime.today()
    turtle.hideturtle()
    skip(65)
    turtle.write(get_week(t), align='center', font=('Times new romen', 14, 'bold'))
    skip(-130)
    turtle.write(t.strftime("%Y.%m.%d"), align='center', font=('Times new romen', 14, 'bold'))
    skip(65)
    turtle.tracer(False)
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60
    hour = t.hour + minute / 60

    second_hand.setheading(6 * second)
    minute_hand.setheading(6 * minute)
    hour_hand.setheading(30 * hour)
    turtle.tracer(True)
    turtle.ontimer(run, 200)


turtle.tracer(False)
turtle.mode('logo')
second_hand = create_hand(135, 'second_hand')
minute_hand = create_hand(125, 'minute_hand')
hour_hand = create_hand(90, 'hour_hand')
draw_clock()
run()
turtle.mainloop()
