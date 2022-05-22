from 实验10_1 import student   #导入类
class substu(student):
    def getCName(self):#返回班级名称
        return '20'+self.xh[:2]+'级'+self.xh[2]+'班'
f=open('data10-1.txt')
s=[]#用列表存储student对象
f.readline()#读出标题行
for r in f:#读出学生数据
    d=r.split(',')
    s.append(substu(d[0],d[1],int(d[2])))#创建对象加入列表
f.close()
def kf(a):#返回对象的班级名称和成绩用于排序
    w=a.getCName()
    w+='%03d' % (100-a.cj)      #成绩按从高到底排序，转换为3位字符串，前面用0占位
    return w  
s.sort(key=kf)
print('%-8s'%'班级','%-5s'%'学号','%-6s'%'姓名','成绩')
for a in s:
    xm='{0:{1}<4}'.format(a.xm,chr(12288))
    print('%-9s%-8s%-6s%d' %(a.getCName(),a.xh,xm,a.cj))
             
