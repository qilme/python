def fsum(a):
   s=0
   for n in a:
      s+=n
   return s#①
b,*a=eval(input('请输入n个数：'))
a.append(b)#②
print(fsum(a))
