import math
a=eval(input('请输入三角形边长a：'))
b=eval(input('请输入三角形边长b：'))
c=eval(input('请输入三角形边长c：'))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('面积=',S)
