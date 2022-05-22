a=input('请输入一串英文字符：')
d=list(a)     					#将字符串转换为列表
n=0
for c in d:   					#执行加密操作
   d[n]=chr(ord(c)+3)			#获得字符的ASCII码，加3，再转换为字符
   n+=1
print('加密后：',end='')
for c in d:
   print(c,end='')
