from random import randrange
class cipher:   #定义密码父类 
    def __init__(self):#初始化，定义密码长度为5，密码字符集为小写字母
        self.length=5
        self.chars='abcdefghijklmnopqrstuvwxyz'
    def getCipher(self):   #根据密码长度和密码字符，随机生成一个密码
        s=''
        for n in range(self.length):
            s+=self.chars[randrange(len(self.chars))]
        return s      
class sub_cipher(cipher):  #定义密码子类
    def setLength(self,n):#设置密码长度为n
        self.length=n
    def setChars(self,s):#设置密码字符集为s
        self.chars=s
if __name__=='__main__':
    print('模块独立运行的自测试输出：')
    x=cipher()      #创建实例对象
    print('cipher实例对象使用默认设置生成的密码：',x.getCipher())
    y=sub_cipher()
    print('sub_cipher实例对象使用默认设置生成的密码：',y.getCipher())
    y.setLength(8)
    y.setChars('1234567890!@#$%^&*')
    print('sub_cipher实例对象使用自定义设置生成的密码：',y.getCipher())
