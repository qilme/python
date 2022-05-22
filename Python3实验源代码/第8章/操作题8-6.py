from random import randint
def f(n):                 		#判断n是否为素数,是素数返回True,否则返回False
  for a in range(2,n//2):
    if n%a==0:
      return False
  return True
c=0
while c<10:
  x=randint(10,1000)    
  while x%2!=0:           		#获得一个随机偶数
    x=randint(10,1000)
  c+=1                    		#对偶数计数
  #分解偶数
  ok=False
  for n in range(2,x//2+1):
    if f(n) and f(x-n):			#n和x-n均为素数时,输出结果
      print('%3d'%x,'=','%3d'%n,'+',x-n)
      ok=True
      break
  if not ok:
    print(x,'不能分解为两个素数和.') 
