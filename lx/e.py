def s(n):
    if n == 0:
        return 1
    else:
        return n*s(n-1)


a = int(input('输入一个整数:'))
sum = 1
for i in range(1, 1 + a):
    sum += 1/s(i)
print(sum)
