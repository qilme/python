a=input('请输入一串字符（不少于4个）：')
b=tuple(a)                  #用字符串创建元组
print('元组：',b)
print('首2元素：',b[:2])
print('尾2元素：',b[-2:])
c=[]
for i in b:
    if i not in c:
        print(i,'：%s次'%b.count(i))
        c.append(i)
    
