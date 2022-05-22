n=int(input('请输入n：'))
a=b=1
print(1,1,end='')
for x in range(1,n-1):#①
   print('',a+b,end='')
   a,b=b,a+b#②
