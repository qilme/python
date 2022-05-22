n=0
print('大于100的10个对偶数：')
for a in range(100,1000):
    if a//100==a%10:        #判断百位和个位是否相等
        print(a,end=' ')    #输出对偶数
        n+=1                #计数
    if n==10:
        break               #已输出10个对偶数时，结束for循环
