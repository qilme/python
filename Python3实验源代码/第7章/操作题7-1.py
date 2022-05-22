f=open('d:/test7-1.txt', 'w')#①
for n in range(1,6):
   c=input('请输入第%s行字符：'%n)
   f.write(c+'\n')#②
f.close()
