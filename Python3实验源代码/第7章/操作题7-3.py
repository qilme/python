f=open('test7-3.txt','r+')
a=f.read()
print('原数据：',a)
a=list(a)#①
n=0
for c in a:
   if 'a'<=c<='z':
      a[n]=chr(ord(c)+3)
   n=n+1
a=''.join(a)
print('转换后：',a)
f.seek(0)
f.write(a)#②
f.close()
