def f(n):
   for i in range(2,n//2):
      if n%i==0:
         return False      	#n被i整除，不是素数，返回False
   return True             	#n是素数，返回True
n=0
print('[10,100]范围内的素数:')
for x in range(10,100):
   if f(x):
      print(x,'',end='')
      n+=1
      if n%10==0:
         print()
