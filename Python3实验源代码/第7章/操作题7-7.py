f=open('test7-7.txt')
d=[]
for b in f:             				#按行迭代文件
   (*a,)=eval(b)         				#将每行中的数据以列表方式赋值给变量a   
   d.append(a)          				#添加到列表
f.close()
r,c=d[0][0],d[0][1]     				#获得稀疏矩阵行列值
x=[]          						#初始化稀疏矩阵
for n in range(r):
   x.append([0]*c)

del d[0]
for r in d:						#将非0值填入稀疏矩阵
   x[r[0]-1][r[1]-1]=r[2]   
#输出稀疏矩阵
for r in x:
   for c in r:
      print('%-4s'%c,end='')
   print()
