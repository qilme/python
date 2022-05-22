import math
class Triangle:
    def __init__(self,a,b,c):         #初始化函数
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=(self.a*self.b*math.sin(math.radians(self.c)))/2
        print("边长：%s，%s  夹角：%s度  面积：%.2f"%
              (self.a,self.b,self.c,s))
x=Triangle(3,4,90)#创建实例对象时提供参数初始化对象
x.area()#调用方法输出三角形面积
