a=input('请输入水果名称：')
b=input('请输入水果价格：')
al=a.split(' ')
bl=b.split(' ')
p=[]
for i in bl:
    p.append(eval(i))
ds=dict(zip(al,p))

print('字典：',ds)
a=input('请输入水果名称：')
if a in ds:
    print(a,'的价格为：',ds.get(a))
else:
    print(a,'不在字典中')
