from time import strftime
from tkinter import *
root=Tk()
root.title('实时日期时间')
t=StringVar()
label1=Label(textvariable=t,font=('宋体',18))#创建绑定变量的标签
label1.pack()
def f():
    def update():
        t.set(strftime('%Y-%m-%d %H:%M:%S %p'))
        root.after(1000,update)			    #递归调用,更新绑定变量
    update()
f()         										#调用函数更新时间
mainloop()
