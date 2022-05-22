#为方便排序，使用嵌套列表来保存数据。
d=[ ["101607",'吴姣','女','学前教育'],
    ["101704",'张思思','女','学前教育'],
    ["701321",'蔡鸿羽','男','电气自动化技术'],
    ["180422",'甘雨婷','女','电气自动化技术'],
    ["111102",'陈鹏涛','男','电子商务'],
    ["701220",'杜建辉','男','电子商务']]

print('使用普通文件读写方法读写CSV文件')
f=open('data7-3-1.txt','w')  #创建文本文件
f.write('准考证号,姓名,性别,专业\n')
for a in d:
    f.write(','.join(a)+'\n')   #加分隔符逗号和换行符输出
f.close()
print('数据已存入文件：data7-3-1.txt')
f=open('data7-3-1.txt','r')   #打开文件，读数据
ds=f.readlines()
f.close()
n=0
for a in ds:
   ds[n]=a.split(',')
   n+=1
def ks(a):          #返回子列表的第0项用于排序
    return a[0]
d0=ds[0]
del ds[0]           #标题行不参与排序
ds.sort(key=ks)
xb='{1:{0}<4}{2:{0}<3}'.format(chr(12288),'姓名','性别')
print('%-6s'%'准考证号',xb,'专业')
for x in ds:        #输出排序后的数据
    xb='{1:{0}<4}{2:{0}<3}'.format(chr(12288),x[1],x[2])
    print('%-10s'%x[0],xb,x[3].strip())

print('\n使用csv模块方法读写CSV文件')
import csv
f=open('data7-3-2.txt','w')  #创建文本文件
cw=csv.writer(f)		#创建常规写对象
cw.writerow(['准考证号','姓名','性别','专业'])
for a in d:
    cw.writerow(a)
f.close()
print('数据已存入文件：data7-3-2.txt')
f=open('data7-3-2.txt','r')  #打开文件，读数据
cr=csv.reader(f)		#创建读取器对象
ds=[]
for r in cr:
    if len(r)>1:
        ds.append(r)            #将非空行数据加入列表
def ks(a):          #返回子列表的第1项用于排序
    return a[1]
d0=ds[0]
del ds[0]           #标题行不参与排序
ds.sort(key=ks,reverse=True)
xb='{1:{0}<4}{2:{0}<3}'.format(chr(12288),'姓名','性别')
print('%-6s'%'准考证号',xb,'专业')
for x in ds:        #输出排序后的数据
    xb='{1:{0}<4}{2:{0}<3}'.format(chr(12288),x[1],x[2])
    print('%-10s'%x[0],xb,x[3].strip())
