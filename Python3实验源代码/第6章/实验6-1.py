def isprime(n):
    f=True
    for a in range(2,n):
        if n%a==0:
            f=False     #n被a整除，不是素数
            break
    return f
print('100以内的素数：')
for a in range(1,100):
    if isprime(a):
        print(a,'',end="")
