def f(a):
   m=len(a)//2				#获得中间位置   
   for n in range(m):
     if len(a)%2==0:
        a[n],a[m+n]=a[m+n],a[n]	        #互换
     else:
        a[n],a[m+n+1]=a[m+n+1],a[n]	  #互换 
   return a
(*b,)=eval(input('请输入多个数据：'))	#将输入的多个数据作为列表赋值给变量b
b=f(b)					#调用函数完成互换
print('对换后：')
for r in b:
   print(r,'',end='')
