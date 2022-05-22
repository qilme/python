f=open('test7-9.txt') 
d=f.read()
(*data,)=eval(d)     				#读出数据，存入列表
f.close()
print('排序前：',end='')
for a in data: 
  print(a,end=' ')
n=len(data)
for i in range(n-1):       			#冒泡法排序
  for j in range(n-i-1):
    if data[j]>data[j+1]:
      t=data[j]
      data[j]=data[j+1]
      data[j+1]=t
print('\n排序后：',end='')
for a in data: 
  print(a,end=' ')
