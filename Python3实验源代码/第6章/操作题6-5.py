def f(a):   		#参数a是表示矩阵的列表对象
   r=len(a)       	#获得原矩阵的行数
   c=len(a[0])    	#获得原矩阵的列数   
   b=[]           	#用列表保存转置矩阵
   for n in range(c):   #初始化转置矩阵
      b.append([0]*r)
   for i in range(r):	#完成矩阵转置
      for j in range(c):
         b[j][i]=a[i][j]   
   return b
a=input('请输入原矩阵：')
a=a.split(' ') 		#按空格分解为列表，先分解出每行的数据
for n in range(len(a)):	#分解行中的每列的数据
   a[n]=a[n].split(',')
print('原矩阵：')
for r in a:             #遍历行
   for c in r:          #遍历行中的元素
      print('%-4s'%c,end='')#每个数据占4列，左对齐，不换行
   print()                 #每行输出之后换行
b=f(a)
print('转置矩阵：')
for r in b:
   for c in r:
      print('%-4s'%c,end='')
   print()
