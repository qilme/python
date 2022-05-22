n=int(input('请输入n：'))
s=1#①
x=1
for i in range(1,n+1):
   x*=i#②
   s+=1/x
print('e=',s)
