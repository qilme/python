a=input('请输入一组词语（空格分隔）：')
ds=a.split(' ')      	  			#将字符串分解为列表
cs={}
for c in ds:            #迭代列表中的词语
   cs[c]=cs.get(c,0)+1 #get(c,0)从词典中取c的映射值（即次数，没有时取0）再加1
for k in cs:
   print(k,':',cs[k])  #输出词语即次数
