from tkinter import *
finfo=Frame()           				#用框架包含输入组件和对应的提示标签
finfo.pack()
uid=StringVar()	        				#用于绑定用户名输入组件
pwd=StringVar()	        				#用于绑定密码输入组件
label1=Label(finfo,text='用户名：',width=8,anchor=E)
label1.grid(row=1,column=1)
entry1=Entry(finfo,textvariable=uid,width=20)		#用户名输入组件
entry1.grid(row=1,column=2)

label2=Label(finfo,text='密%s码：'%chr(12288),width=8,anchor=E)	
label2.grid(row=2,column=1)
entry2=Entry(finfo,show='*',textvariable=pwd,width=20)	#密码输入组件
entry2.grid(row=2,column=2)

def done():     										#确定按钮命令函数    
    msg.config(text='你输入的用户名为：%s，密码为：%s'%(uid.get(),pwd.get()))
bt1=Button(text='确定',command=done)
bt1.pack()
msg=Label()
msg.pack()
mainloop()
