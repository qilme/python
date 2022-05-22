a,b,c=eval(input('请输入3个数：'))
if a<b:
    a,b=b,a
if a<c:
    a,c=c,a
if b<c:
    b,c=c,b
print(a,b,c)
