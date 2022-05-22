import jieba.posseg as ps
s='早餐吃了意大利通心粉'
r=ps.cut(s)
for a in r:  
   print('%s\t%s'%(a.word,a.flag))
