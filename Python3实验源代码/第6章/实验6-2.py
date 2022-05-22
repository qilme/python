def fsum(*n):
    s=0
    for a in n:
        s+=a
    return s
a=input('请输入多个数据：')
b='fsum(%s)'%a              #构造函数调用表达式
print('和 =',eval(b))
