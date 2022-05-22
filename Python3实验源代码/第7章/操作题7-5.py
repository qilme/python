f=open('test7-5.txt')
for b in f:             			#按行迭代文件
   b=b.strip()          			#去掉行尾的换行符号
   for c in b:
      if c<'0':         			#c是运算符时，处理输出
         n=b.index(c)   			#获得运算符的位置
         print('%2s'%b[:n],c,'%-2s'%b[n+1:],'=',eval(b)) #设置宽度以便对齐
         break
f.close()
