f=open('test7-4.txt')
a=f.read()
(*a,)=eval(a)#① 
print('原数据：',end='')
for b in a:
   print(b,'',end='')
a.sort() #②
print('\n排序后：',end='')
for b in a:
   print(b,'',end='')
f.close()
