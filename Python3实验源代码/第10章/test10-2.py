class test:
    data=0
x=test()
y=test()#1
x.data=100
test.data=20#2
print(x.data,y.data,test.data)
