def f(a,b):   
   c=a.replace(b,'')    		#删除字符串包含的字符串b
   return repr(c)
n=0
x=input('请输入字符串减法表达式：')
c=x.split('-')          		#分解字符串表达式
print(x,'=',f(eval(c[0]),eval(c[1])))	#使用eval()获得字符串中的字符串
