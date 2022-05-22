import jieba.analyse as an
import jieba
f=open('d:/三国演义.txt',encoding='utf-8')
s=f.read()                      #读出文件内容到字符串中
f.close()
r=an.extract_tags(s,10,False,('nr',))          #返回前10个人名
for k in r:  
   print(k,end=' ')
