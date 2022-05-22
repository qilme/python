import jieba.analyse as an
import jieba
f=open('d:/test9-7.txt',encoding='utf-8')
s=f.read()      #读出文件内容到字符串中
f.close()
jieba.add_word('区块链')
r=an.extract_tags(s,5)#返回前5个关键词
for k in r:  
   print(k,end=' ')
