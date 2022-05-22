a=input('请输入多个数(逗号分隔)：')
b=eval('{'+a+'}')
print('原集合：',b)
c=eval(input('请输入一个数：'))
if c in b:
   b.remove(c)
   print('已从集合删除',c)
else:
   b.add(c)
   print(c,'已添加到集合')
print('新集合：',b)
