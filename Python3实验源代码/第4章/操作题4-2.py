a=input('请输入一串字符：')
b=list(a)
print('原列表：',b)
b=list(set(b))
b.sort()
print('排序后：',end='')
for c in b:
   print(c,end='')
