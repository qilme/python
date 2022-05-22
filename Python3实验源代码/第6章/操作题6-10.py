def f(x):   
   s=0
   for n in x:             			#求和
      s+=n
   return s/len(x)         			#返回平均值
c=input('请输入n个数值：')
(*x,)=eval(c)              			#将字符串中的多个数值作为列表赋值为x
c=c.replace(',','+')       			#准备输出的加法表达式
print(c+'的平均值 =',f(x))
