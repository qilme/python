f=open('test7-6.txt',encoding='utf-8')
d=[]
t=next(f)               			#读出标题行
for b in f:             			#按行迭代文件
   b=b.split(',')       			#按逗号分解为列表
   b[2]=int(b[2])       			#将成绩字符串转换为整数
   b[3]=int(b[3])
   b[4]=int(b[4])
   b.append(sum(b[2:])) 			#计算总分
   d.append(b)

def fk(a):
   return a[5]          			#返回子列表的总分用于排序
d.sort(key=fk,reverse=True)
n=1
#输出时注意对齐
xm='{1:{0}<4}'.format(chr(12288),'姓名')
print(' %-4s%-5s%s %-4s %-4s %-4s %s'
      %('名次','学号',xm,'语文','数学','外语','总分'))
for a in d:
   print('{0:^6d}'.format(n),'%-6s'% a[0],
         '{1:{0}<4}'.format(chr(12288),a[1]),
         '%-7s%-7s%-7s%s' %tuple(a[2:]))
   n+=1 						#计算名次
f.close()
