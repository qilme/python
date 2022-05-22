n=int(input('请输入正整数n：'))
#用列表表示nxn的矩阵下半部分，各元素初始化为1
d=[]
for a in range(n):
   x=[1]
   for b in range(a):
      x.append(1)
   d.append(x)
for i in range(2,n):
   for j in range(1,i):
      d[i][j]=d[i-1][j]+d[i-1][j-1]#计算非1元素
for a in d:							
   for b in a:
      print('%-6d'%b,end='') 	#输出，每个元素宽度为6
   print()
