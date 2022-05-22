n=int(input('请输入n：'))
s=1
x=2
while x<=n:#①
   s*=x
   x+=1#②
print('%s! ='%n,s)
