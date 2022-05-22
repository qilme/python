#将姓名和成绩以二元组的方式存入列表
s=[('Powell',9.74),('Green',9.79),('Bolt',9.69),('Burrell',9.85),('Montgomery',9.78),('Lewis',9.86)]
def gets(a):					#返回元组的第2个元素，即成绩
   return a[1]
s.sort(key=gets)				#指定列表排序关键字函数，用二元组中的成绩排序
n=1
print("%-4s%-10s成绩" % ('名次','姓名'))	
for k,v in s:
   print("%-6s%-12s%s" %(n,k,v))	#格式化输出名次、姓名和成绩
   n+=1							#计算名次
