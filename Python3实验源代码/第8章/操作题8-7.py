from random import *
def f(n):                 				#判断n是否为素数
  for a in range(2,n//2):
    if n%a==0:
      return False
  return True
def divs(n):              				#返回n的因子列表，不包含1和n
  d=[]
  for x in range(2,n):
    if n%x==0:
      d.append(x)
  return d
n=0
cf='+-*/'
while n<20:
  c=sample(cf,1)[0]       				#获得运算符
  if c in '+*':
    a=randint(10,99)
    b=randint(10,99)
  elif c=='-':
    a=randint(10,99)
    b=randint(10,a)
  else:
    a=randint(10,99)
    while True:           
      if f(a):            				#a是素数时，重新获得一个随机数
        a=randint(10,99)     
      else:
        ds=divs(a)         				#获得a的因数列表
        b=sample(ds,1)[0]
        break             				#找到符合条件数，结束循环
  print(a,c,b)
  n+=1
