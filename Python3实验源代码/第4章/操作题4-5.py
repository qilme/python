a=input('请输入一串字符：')
b=list(set(a))					#获得不重复字符的列表
b.sort()						#对不重复字符排序
cs=[]
n=0
for c in b:
   cs.append((c,a.count(c)))		#将字符及次数作为元组添加到列表
   n=n+1
for k,v in cs:					#迭代列表中的元组
   print(k,':',v)			
