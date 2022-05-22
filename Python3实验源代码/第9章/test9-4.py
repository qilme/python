import jieba
s='程序员工会推出一项措施促进Python语言的推广'
jieba.add_word('程序员工会')
jieba.add_word('Python语言')
r=jieba.cut_for_search(s)
print(' '.join(r))
