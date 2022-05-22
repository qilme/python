import jieba
import jieba.analyse
import wordcloud
import tkinter
from PIL import Image,ImageTk
file=open('红楼梦.txt',encoding='utf-8')       		#指定编码确保正确分词
str=file.read()
file.close()
cast=jieba.analyse.extract_tags(str,topK=100,allowPOS=('nr',)) 	#筛选前100的人名
wlist=jieba.lcut(str)                           		#分词，获得词语列表
text=' '.join(wlist)
print(text)
wtimes={}           
for a in wlist:                                 		#统计词语出现的次数
    if a in cast:
        wtimes[a]=wtimes.get(a,0)+1             		#将词语加入字典、计数
wlist=list(wtimes.keys())
wlist.sort(key=lambda x:wtimes[x],reverse=True) 	#按数量从大到小排序
for a in wlist[:10]:								#输出出场数最多的前10名
    print(a,wtimes[a],sep='\t')

cloud=wordcloud.WordCloud(font_path='simsun.ttc',background_color='white'
                           ,width=800,height=600).generate(text)  #生成词云
file=cloud.to_file('redcloud.png')  				#将词云写入图片
root=tkinter.Tk()                   				#创建Tk窗口
img=Image.open('redcloud.png')      				#打开词云图片
pic=ImageTk.PhotoImage(img)
imgLabel=tkinter.Label(root,image=pic)				#将词云作为标签图片
imgLabel.pack()                         				#打包标签
root.mainloop()
