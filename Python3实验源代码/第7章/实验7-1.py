x=input('请输入诗句内容：')
x=x.split(' ')                  #分解为列表
f=open('data7-1.txt','w')    #创建文件，写入数据
for c in x:
    f.write(c)
    f.write('\n')
f.close()
f=open('data7-1.txt')        #打开文件，读数据
d=f.readlines()
print(' '*6,'春晓')
del d[0]
for c in d:
    print('{0:{1}^10}'.format(c.strip(),chr(12288)))
f.close()
