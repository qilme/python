def s(n):
    if n  == 1:
        return 1
    else:
        return n*s(n-i)
a=eval(input('输入一个正整数'))
list=[]
for i in range(1,a+1):
    list.append(s(i))
    Sum = 1
for i in range(1,a+1):
    Sum +=1/s(i)
print(Sum)
