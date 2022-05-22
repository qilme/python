import jieba
s='早餐吃了意大利通心粉'
r=jieba.tokenize(s)
for a in r:  
   print('%s\t%s\t%s'%(a[0],a[1],a[2]))
