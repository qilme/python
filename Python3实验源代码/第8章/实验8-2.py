from random import randint
a=[]
for n in range(10):
    a.append(randint(10,99))
a.sort()
for n in a:
    print(n,'',end='')
