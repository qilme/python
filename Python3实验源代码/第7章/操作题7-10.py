import csv
f=open('test7-10.csv')
cr=csv.DictReader(f)
d={}                    				#用字典对象来统计总数量和总金额
for r in cr:
   zs=zj=0
   if r['编号'] in d:
      zs=d[r['编号']]['总数量'] 		#获得现有数据
      zj=d[r['编号']]['总金额'] 
   zs+=int(r['数量'])
   zj+=int(r['数量'])*float(r['单价'])
   d[r['编号']]={'商品名称':r['商品名称'],'总数量':zs,'总金额':zj} #存入字典
f.close()

ds=list(d.items())   				#字典转换为列表
def fk(a):
   return a[0]       				#返回列表第0项，即编号字段用于排序
ds.sort(key=fk)      				#排序
f=open('test7-10-2.csv','w')
cw=csv.DictWriter(f,fieldnames=['编号','商品名称','总数量','总金额'])
cw.writeheader()				#写入字段名
for r in ds:
   r[1]['编号']=r[0]            		#将编号加入字典             
   cw.writerow(r[1])             		#将字典写入csv文件
f.close()
print('数据以写入文件test7-10-2.csv')
