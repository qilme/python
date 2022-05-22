from turtle import *


def dl(draw):
    if draw:
        pd()
    else:
        pu()
    fd(100)
    rt(90)


def dg(d):
    dl(True) if d in [2, 3, 4, 5, 6, 7, 8, 9] else dl(False)
    if d in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        dl(True)
    else:
        dl(False)


dl()
dl()
lt(90)
dl()
dl()
dl()
done()
