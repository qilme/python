f=open('data7-4.txt') 
d=f.read()
(*data,)=eval(d)
f.close()
n=len(data)
for i in range(n-1):
  k=i 
  for j in range(i+1,n):
    if data[j]<data[k]:
      k=j   
  if i!=k:      
    t=data[i]
    data[i]=data[k]
    data[k]=t
print('排序后：',end='')
for a in data: 
  print(a,end=' ')

x=eval(input('\n请输入一个数：'))
start=0
end=len(data)-1
mid=(start+end)//2
while start<=end:
  if data[mid]==x:
    print('%s是第%s个数据'%(x,mid+1))
    break
  else:
    if x<data[mid]:
      end=mid-1
    else:
      start=mid+1
  mid=(start+end)//2  
if start>end:
  print('不包含%s'%x)
