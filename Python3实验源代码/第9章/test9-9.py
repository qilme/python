import jieba.posseg as pseg
import wordcloud
import tkinter
from PIL import Image,ImageTk
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
text=' '.join(cstr)
cloud=wordcloud.WordCloud(font_path='simsun.ttc',background_color='white'
                           ,stopwords=sw,collocations=False
                           ,width=640,height=480).generate(text)  	#生成词云
file=cloud.to_file('redcloud.png')  						#将词云写入图像
root=tkinter.Tk()                   							#创建Tk窗口
img=Image.open('redcloud.png')      						#打开词云图像
pic=ImageTk.PhotoImage(img)
imgLabel=tkinter.Label(root,image=pic)						#将词云作为标签图像
imgLabel.pack()                         						#打包标签
root.mainloop()
