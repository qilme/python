f=open('d:/test7-2.txt', 'w+')#①
c=input('请输入字符串：')
f.write(c)
f.seek(0)#②
a=f.read()
print(a[::-1])
f.close()
