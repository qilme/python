from time import strftime
t=strftime('%Y+%m-%d* %I:%M:%S%p')		#获得格式化的日期时间字符串
t=t.replace('+','年')				#替换字符中的符号
t=t.replace('-','月')
t=t.replace('*','日')
print(t)					#输出正确结果
