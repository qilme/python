a,b=eval(input('请输入两个整数a,b：'))
x,y=a,b
a=max(x,y)
b=min(x,y)
d=a%b
while d!=0:		#余数为0时，b为最大公约数
   a=b
   b=d
   d=a%b
print(' %s , %s 的最大公约数：%s'%(x,y,b))
print(' %s , %s 的最小公倍数：%s'%(x,y,x*y//b))
