import math
class iList:
    def __init__(self,a):         #初始化函数
        self.data=a
    def getMax(self):
        m=self.data[0]
        for a in self.data[1:]:  #找最大值
            if a>m:
                m=a
        return m            #返回最大值
    def getMin(self):
        m=self.data[0]
        for a in self.data[1:]:  #找最小值
            if a<m:
                m=a
        return m            #返回最小值
(*x,)=eval(input('请输入多个整数：'))
n=iList(x)
print('最大值：',n.getMax())
print('最小值：',n.getMin())
