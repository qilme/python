import wordcloud
import cv2
import jieba.posseg as pseg
file=open('三国.txt',encoding='utf-8')       				#指定编码确保正确分词
str=file.read()
file.close()
wlist=pseg.lcut(str)                           				#分词，获得词语列表
wtimes={}           
cstr=[];sw=[]
for a in wlist:                                 					#统计词语出现的次数
    if a.flag== 'nr' :
        wtimes[a.word]=wtimes.get(a.word,0)+1             				#将词语加入字典并计数
        cstr.append(a.word)
    else: sw.append(a.word)
wlist=list(wtimes.keys())
wlist.sort(key=lambda x:wtimes[x],reverse=True) 				#按数量从大到小排序
for a in wlist[:10]:										#输出出场数最多的前10名
    print(a,wtimes[a],sep='\t')
s=' '.join(cstr)
img=cv2.imread('test9-10.jpg')  #读入形状图片
cloud=wordcloud.WordCloud(font_path='simsun.ttc',collocations=False,
                          background_color='white',mask=img,
                          width=480,height=640).generate(s)#创建词云对象，中文字体为“宋体”
file=cloud.to_file('test9-10shape.jpg')#生成词云图片
img2=cv2.imread('test9-10shape.jpg')#读出图片
cv2.imshow('wordcloud',img2)#显示图片
