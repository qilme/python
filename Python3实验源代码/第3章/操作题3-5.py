import math
a,b,c=eval(input('请输入方程的系数a,b,c：'))
d=b*b-4*a*c
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('方程的解x1=%.2f'%x1)
    print('方程的解x2=%.2f'%x2)
if d==0:
    print('方程的解x1=x2=%.2f'%(-b/(2*a)))
if d<0:
    x1=-b/(2*a)
    x2=math.sqrt(-d)/(2*a)
    print('方程的解x1=%.2f+%.2fj'%(x1,x2))
    print('方程的解x2=%.2f-%.2fj'%(x1,x2))
