class student:
    def __init__(self,xh,xm,cj):#定义对象初始化方法
         self.xh=xh
         self.xm=xm
         self.cj=cj
f=open('data10-1.txt')
s=[]#用列表存储student对象
f.readline()#读出标题行
for r in f:#读出学生数据
    d=r.split(',')
    s.append(student(d[0],d[1],int(d[2])))#创建对象加入列表
f.close()
def kf(a):
    return a.cj  #返回对象的cj字段值用于排序
s.sort(key=kf,reverse=True)
print('学号\t姓名\t成绩')
for a in s:
    print('%s\t%s\t%d' %(a.xh,a.xm,a.cj))
             
