f=open('test7-6.txt',encoding='utf-8')
d=[]
t=next(f)               				#读出标题行
for b in f:             				#按行迭代文件
   b=b.split(',')       				#按逗号分解为列表
   b[2]=int(b[2])       				#将成绩字符串转换为整数
   b[3]=int(b[3])
   b[4]=int(b[4])
   b.append(round(sum(b[2:])/3,1)) 	#计算平均成绩
   del b[2:-1]                         #删除各门课程成绩
   d.append(b)
#将列表存入文件test7-8.txt
import pickle	                       #使用pickle模块从文件读写对象
f=open('test7-8.txt','wb')    		#使用二进制文件存储对象
pickle.dump(d,f)		       #将列表对象写入文件
f.close()
print('数据已存入文件：test7-8.txt')
f=open('test7-8.txt','rb')   		#以二进制格式打开文件，读数据
ds=pickle.load(f)                      #读出列表对象
f.close()

def fk(a):
   return a[2]          		#返回子列表的平均分用于排序
d.sort(key=fk,reverse=True)
n=1
#输出时注意对齐
xm='{1:{0}<4}'.format(chr(12288),'姓名')
print(' %-4s%-5s%s %s'
      %('名次','学号',xm,'平均分'))
for a in d:
   print('{0:^6d}'.format(n),'%-6s'% a[0],
         '{1:{0}<4}'.format(chr(12288),a[1]),a[2])
   n+=1 #计算名次
