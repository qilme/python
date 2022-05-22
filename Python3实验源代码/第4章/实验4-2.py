a=input('请输入多个整数：')
b=a.split(',')          #将输入数据转换为列表
n=0
for c in b:
   b[n]=int(c)          #将列表元素转换为整数
   n+=1
print('原始列表：',b)    
m=b.index(max(b))       #获得最大值的位置
x=m-1                   #计算最大值的前一个元素位置
if x<0: 
    x=0
y=m+2
if y>=len(b):           #获得最大值及其相邻元素
    d=b[x:]
else:
    d=b[x:y]
print('最大值及相邻元素：',d)   
x=eval(input('请输入一个数：'))
if x in b:
    print(x,'是第%s个数'%(1+b.index(x)))
    b.remove(x)
    print('已从列表删除',x)
else:
    b.append(x)
    print(x,'已添加到列表')
b.sort()
print('排序后的数据：')
for c in b:
    print(c,end=' ')
