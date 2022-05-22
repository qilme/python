def fact(n):
   s=1
   for a in range(2,n+1):#①
      s*=a
   return s
n=eval(input('请输入n：'))
print('%d! ='%n,fact(n) )#②
