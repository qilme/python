a='123456789'
n=len(a)
m=2
print('%21c'%'1')						#第1行
while m<=n:    
    print(' '*(21-m),end='')				#输出每行前面的空格
    print('{}{}'.format(a[:m],a[m-2::-1]))
    m+=1
