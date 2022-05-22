'''
输入两条直角边长度，求斜边长度。
math.sqrt()用于计算平方根
'''						#（1） 
from math import sqrt      			
a=eval(input('请输入直角边1：'))		#（2）
b=eval(input('请输入直角边2：'))		#（3）
if a<=0:
    print('边长必须是正数')
else:
    if b<=0:
        print('边长必须是正数')
    else:
        print('斜边=',sqrt(a*a+b*b))	        #（4）
