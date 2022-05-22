class numeric:
    def __init__(self,a,b):
        if ( type(a)!=type(1) and type(a)!=type(1.0))\
            or (type(b)!=type(1) and type(b)!=type(1.0)):
            raise TypeError("参数类型错误：请提供整数或浮点数作为参数！")
        else:
            self.x=a
            self.y=b
    def add(self):
        print("%s + %s = %s"%(self.x,self.y,self.x+self.y))
x=numeric(12,2.3)
x.add()
