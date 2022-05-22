import jieba
s='程序员工会推出一项措施促进Python语言的推广'
r=jieba.cut(s)                  #默认使用精确模式分词
print('精确模式：',' '.join(r))
r=jieba.cut(s,True)             #使用全模式分词
print('全模式：',' '.join(r))
