def f(a,b):
   c=[[0,0],[0,0]]         			#创建保存乘法结果的列表
   for i in range(2):				#遍历结果列表,计算各个元素值
      for j in range(2):
            c[i][j]=a[i][0]*b[0][j]+a[i][1]*b[1][j]
   return c
x=input('请输入矩阵A：')			#输入数据为字符串
a=x.split(' ')
a[0]=list(eval(a[0]))   			#将字符串表示的第1行数据转换为列表
a[1]=list(eval(a[1]))   			#将字符串表示的第2行数据转换为列表
x=input('请输入矩阵B：')
b=x.split(' ')
b[0]=list(eval(b[0]))
b[1]=list(eval(b[1]))
x=f(a,b)
print('矩阵A：')				#输出矩阵
for r in a:
   for c in r:
      print('%-4s'%c,end='')
   print()
print('矩阵B：')
for r in b:
   for c in r:
      print('%-4s'%c,end='')
   print()
print('A×B=')
for r in x:
   for c in r:
      print('%-4s'%c,end='')
   print()

