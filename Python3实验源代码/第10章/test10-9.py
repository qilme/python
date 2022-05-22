from random import randint
class test:
    __count=0               #“私有”属性记录实例对象个数
    def __init__(self):
        test.__count+=1
    @staticmethod
    def getCount():         #定义静态方法返回实例对象个数        
        return test.__count      
x=test()#创建实例对象
y=[]
for n in range(randint(1,10)):#创建随机个数的实例对象
    y.append(test())
print('通过类对象返回的实例对象个数：',test.getCount())
print('通过实例对象返回的实例对象个数：',x.getCount())
