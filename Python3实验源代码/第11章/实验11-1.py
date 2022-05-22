#从tkinter模块导入类
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import *
'''
初始化全局变量：thisFileName
thisFileName保存当前操作的文件名。根据thisFileName是否为空判断当前是否正在处理成绩数据，从而执行相应的保存操作。
'''
thisFileName=''
'''
初始化全局变量：scaleOption
scaleOption保存平时成绩、期中成绩、期末成绩在总成绩中的占比
在设置比例时，将设置保存在scaleOption中。
在计算总成绩时，访问scaleOption，根据比例计算。
'''
scaleOption=[0.1,0.2,0.7]
root=Tk()                       #创建主窗口
root.title('成绩管理系统')      #设置窗口标题
style = ttk.Style()
style.configure("Treeview.Heading", foreground='#0000FF')	#设置表格标题栏文字颜色
#用LabelFrame包含Treeview和Scrollbar，用Treeview创建表格
fmain=LabelFrame(text='数据：')
fmain.pack(anchor=W,expand=YES,fill=BOTH)
columns = ('学号','姓名','平时成绩','期中成绩','期末成绩','总成绩')
treeview = ttk.Treeview(fmain,show="headings", columns=columns)  #创建表格
for c in columns:
    treeview.column(c,width=100,  anchor='center')  #定义列
    treeview.heading(c, text=c)                     #定义列标题
treeview.pack(side=LEFT,expand=YES,fill=BOTH)
sc=Scrollbar(fmain,orient=VERTICAL)                 #创建滚动条
sc.pack(side=RIGHT,fill=Y)
sc.config(command=treeview.yview)                   #将滚动条关联到表格
treeview.config(yscrollcommand=sc.set)              #为表格绑定滚动条
'''
treeview_sort_column(table, col, reverse)
单击表格列标题时对该列进行排序。
table：参数为表格对象。
col：要排序的列的名称
reverse：sort()方法排序的reverse参数值，为True时按从大到小排序，为False时按从小到大排序。
'''
def treeview_sort_column(table, col, reverse):
    #使用列数据创建用于排序的列表，列表元素格式(单元格值,item编号)
    #例如[('94', 'I001'), ('87', 'I002'), ……]。
    ldata = [(table.set(k, col), k) for k in table.get_children()]    
    colname = ('平时成绩','期中成绩','期末成绩','总成绩')
    def kf(a):
        return eval(a[0]) #成绩按数值进行排序
    if col in colname:
        ldata.sort(key=kf,reverse=reverse)          #各个成绩列排序
    else:
        ldata.sort(reverse=reverse)                 #学号、姓名列排序    
    for index, (val, k) in enumerate(ldata):        #enumerate()可为迭代项添加序号index       
        table.move(k, '', index)                    #根据排序后的索引创新排列表格数据
    # 重建标题，再次单击可以相反的顺序排序
    table.heading(col, command=lambda: treeview_sort_column(table, col, not reverse))  
#为表格的列标题绑定函数，使列可排序
for col in columns:
    treeview.heading(col, text=col, command=lambda _col=col:
                     treeview_sort_column(treeview, _col, False))
'''
edit_cell(event)
执行单元格编辑操作,绑定为表格的双击事件函数。
event：事件对象。利用event.x和event.y确定鼠标位置，在该位置显示编辑组件。
'''
def edit_cell(event): 
    if len(treeview.selection())<1:
        return                                      #单击标题栏时不执行编辑操作
    thisitem=treeview.selection()[0]                #获得选中项的id，如“I001”，id后3位是16进制的行号
    item_text = treeview.item(thisitem, "values")   #获得选中项的值列表
    column= treeview.identify_column(event.x)       #返回双击单元格所在的列名
    row = treeview.identify_row(event.y)            #返回双击单元格所在的行名
    cn = int(str(column).replace('#',''))           #获得列号
    rn = int(str(row).replace('I',''),16)           #获得行号
    ftool=Frame(root)                               #创建单元格编辑工具栏
    def exitedit(event):
        ftool.destroy()                             #删除组件
    ftool.bind('<FocusOut>',exitedit)               #失去焦点执行删除组件操作
    ftool.place(x=event.x,y=event.y)                #在鼠标单击位置显示编辑组件
    text=StringVar()
    entryedit = Entry(ftool,textvariable=text)      #绑定到StringVar变量，便于获取输入值
    text.set(item_text[cn-1])                       #将单元格的值显示到输入框
    entryedit.pack(side=LEFT)                       #将输入框添加到编辑工具栏
    def saveedit():                                 #保存修改，并删除编辑组件
        treeview.set(thisitem, column=column, value=text.get())        
        ftool.destroy()
    def escedit():                                  #取消修改，并删除编辑组件
        ftool.destroy()    
    okb = ttk.Button(ftool, text='确定', width=4,command=saveedit)
    okb.pack(side=LEFT)
    escb = ttk.Button(ftool, text='取消', width=4,command=escedit)
    escb.pack(side=LEFT)    
    entryedit.focus_set()                           #令编辑框获得焦点
treeview.bind('<Double-1>', edit_cell)              #为表格双击事件绑定函数，执行编辑操作
'''
updateRecent()：更新最近访问的文件菜单
从文件recentfiles.txt中读出最近访问的文件清单，用于创建“最近”菜单项。
'''
def updateRecent(): 
    f=open('recentfiles.txt')                       
    fs=f.readlines()                                    #读取文件中的最近访问文件清单
    f.close()
    mfile.delete(3)                                     #删除原来的“最近”菜单项    
    recent=Menu()
    mfile.insert_cascade(3,label='最近',menu=recent)    #重建“最近”菜单项
    n=1    
    for c in fs:
        c=c.strip()
        recent.add_command(label=str(n)+'、'+c,
            command=lambda _fname=c:openFile(_fname))   #将文件名作为函数参数
        n+=1
'''
newFile()：清除表格现有数据和当前文件记录
'''
def newFile():
    global thisFileName
    items=treeview.get_children()
    if len(items)>0:#表单中有数据时，提示执行保存操作
        y=askyesno('提示','是否保存正在处理的数据？')
        if y:
            mfile.invoke(5)          #调用“保存”菜单项绑定的函数执行保存操作
    thisFileName=''                  #清空记录的文件名
    fmain.config(text='数据：')      #恢复表格标题栏
    for n in treeview.get_children():#删除表格中的全部数据
        treeview.delete(n)
    treeview.update()
'''
openFile(fn=None)
fn：为文件名，未指定参数时，用askopenfilename()显示对话框选择要处理的文件。
函数从文件中读出数据，显示到表格中。
'''
def openFile(fn=None):
    if fn!=None:
        fname=fn                #指定文件名时，将其作为要处理的文件名
    else:
        fname=askopenfilename() #用对话框选择要处理的文件
        if fname=='':
            return              #未选择文件时，不执行后继操作
    global thisFileName         #声明全局变量后，才能在函数中为其赋值
    thisFileName=fname          #记录当前操作的文件名
    data=[]                     #创建用于存放文件数据的列表
    try:
        f=open(fname)
        for r in f:
            r=r.strip()         #去掉数据末尾的换行符
            d=r.split(',')      #用逗号作为分隔符分解字符串
            d.append('')        #原文件中可能没有“总成绩”字段，用空字符占位
            data.append(d)      #将保存一行数据的列表作为元素添加到总数据列表中
        f.close()
        data[0][5]='总成绩'
        rows=len(data)          #获得总的数据行数量
        cols=6                  #每行数据最多6列 
        for n in treeview.get_children():
            treeview.delete(n)      #清除现有数据
        for i in range(1,rows):     #将数据添加到表格
            treeview.insert('', i,text='r%s'%i, values=data[i][:cols])
        fmain.config(text='数据：'+fname)
        updateRecentFiles(fname)    #更新访问的文件列表
    except:
        msg='%s\n文件格式错误！文件基本格式如下：'%fname+\
            '\n学号,姓名,平时成绩,期中成绩,期末成绩'+\
            '\n19001,王瑶,94,78,89'+\
            '\n……'
        showerror('文件格式错误',msg)
'''
updateRecentFiles(fname)：
fname：当前访问的文件名，将其添加到recentfiles.txt的第一行。
同时，调用updateRecent()更新“最近”菜单。
'''
def updateRecentFiles(fname):
    f=open('recentfiles.txt')
    fs=f.readlines()
    f.close()
    for n in range(len(fs)):
        fs[n]=fs[n].strip()         #去掉字符串末尾的换行符
    if fname in fs:
        fs.remove(fname)            #将原有的文件名删除
    fs.insert(0,fname)              #当前文件名添加为第1项
    f=open('recentfiles.txt','w')   #用新的文件清单覆盖原文件
    for c in fs[:10]:               #最多保存10条文件访问记录
        print(c,file=f)             #写入文件，print()可换行
    f.close()
    updateRecent()                  #更新菜单
'''
saveRecords()：将表格中的数据存入文件。
'''
def saveRecords():
    if thisFileName!='':
        #有当前操作文件名时，将数据存入该文件
        f=open(thisFileName,'w')
        print('学号,姓名,平时成绩,期中成绩,期末成绩,总成绩',file=f)
        for n in treeview.get_children():
            row=treeview.item(n,"values")
            print(','.join(row),file=f)
        f.close()
        showinfo('保存文件','数据已存入：'+thisFileName)
    else:
        mfile.invoke(6)          #调用“另存为”菜单项绑定的函数保存现有数据
'''
saveAsNew()：将表格中的数据存入新文件。
'''
def saveAsNew():
    global thisFileName
    fnew=asksaveasfilename(filetypes=[('CSV文件','.csv'),],
                initialfile=thisFileName)  #显示另存为对话框，选择保存数据的文件
    if fnew=='':
        return                              #未选择文件时，不执行保存操作    
    f=open(fnew,'w')
    print('学号,姓名,平时成绩,期中成绩,期末成绩,总成绩',file=f)#输出字段名
    for n in treeview.get_children():       #遍历表格的行，将数据存入文件
        row=treeview.item(n,"values")
        print(','.join(row),file=f)
    f.close()
    fmain.config(text='数据：'+fnew)        #更新表格的标题，显示新的文件名    
    thisFileName=fnew                       #记录当前操作的文件名
    updateRecentFiles(fnew)                 #更新访问的文件列表
    showinfo('另存文件','数据已存入：'+fnew)#显示保存提示
'''
delRecord()：删除表格中的当前选中行
'''
def delRecord():
    if len(treeview.selection())<1:
        return      #没有选中项时不执行删除操作
    y=askyesno('提示','是否删除当前记录？')
    if y:
        thisitem=treeview.selection()[0]    #获得选中项的id
        treeview.delete(thisitem)           #删除记录
'''
newRecord()：为表格添加一个空行，用于添加新记录
'''
def newRecord():
    columns = ('新记录','','','','','')
    n=treeview.insert('',0, values=columns) #在表格第1行添加新记录
    treeview.see(n)                         #使其可见 
    treeview.selection_set(n)               #选中该行
'''
doSum()：根据设置，计算总成绩
'''
def doSum():
    for n in treeview.get_children():
        row=list(treeview.item(n,"values"))
        t=int(row[2])*scaleOption[0]+int(row[3])*scaleOption[1]+int(row[4])*scaleOption[2]
        treeview.set(n, column=5, value=str(round(t)))#将总成绩添加到表格
'''
setOption():设置平时成绩、期中成绩和期末成绩在总成绩中所占的比例。
将设置保存到全局变量scaleOption中。
'''
def setOption():
    global scaleOption
    s0=DoubleVar()              #创建绑定变量
    s0.set(scaleOption[0])      #将现有设置设置为绑定变量初始值
    s1=DoubleVar()
    s1.set(scaleOption[1])
    s2=DoubleVar()
    s2.set(scaleOption[2])
    ftool=LabelFrame(root,text='设置成绩比例')  #创建单元格编辑工具栏
    lb1=Label(ftool,text='平时成绩：')
    lb1.grid(row=1,column=1)
    op1 =Entry(ftool,textvariable=s0)           #创建输入框，并关联绑定变量
    op1.grid(row=1,column=2)
    lb2=Label(ftool,text='期中成绩：')
    lb2.grid(row=2,column=1)
    op2 =Entry(ftool,textvariable=s1)
    op2.grid(row=2,column=2)
    lb3=Label(ftool,text='期末成绩：')
    lb3.grid(row=3,column=1)
    op3 =Entry(ftool,textvariable=s2)
    op3.grid(row=3,column=2)    
    def saveedit():#保存修改，并删除编辑组件
        a=s0.get()
        b=s1.get()
        c=s2.get()
        if (a<0) or (a>1) or (b<0) or (b>1) or (c<0) or (c>1) or\
           (a+b+c)>1:
            lb4.config(text='错误:成绩比例设置错误！',fg='red')
        else:
            scaleOption[0]=a
            scaleOption[1]=b
            scaleOption[2]=c
            ftool.destroy()
    def escedit():#取消修改，并删除编辑组件
        ftool.destroy()
    def exitedit(event):#失去焦点，即单击组件之外的任意位置时删除组件
        ftool.destroy()
    ftool.bind('<FocusOut>',exitedit)   #绑定工具栏的失去焦点时间处理函数
    okb = ttk.Button(ftool, text='确定', width=4,command=saveedit)
    okb.grid(row=3,column=3)
    escb = ttk.Button(ftool, text='取消', width=4,command=escedit)
    escb.grid(row=4,column=3)
    lb4=Label(ftool,text='')#用于显示设置提示
    lb4.grid(row=4,column=1)
    ftool.place(x=100,y=20)
    op1.focus_set()         #令编辑框获得焦点

menuroot=Menu(root)                         		#创建菜单
root.config(menu=menuroot)                  		#将菜单添加到主窗口
mfile=Menu()
menuroot.add_cascade(label='文件',menu=mfile)		#添加为级联菜单
mfile.add_command(label='新建',command=newFile)		#添加菜单项，绑定到指定函数
mfile.add_command(label='打开...',command=openFile)
recent=Menu()
mfile.add_cascade(label='最近',menu=recent)
updateRecent()                              #更新最近访问的文件菜单
mfile.add_separator()
mfile.add_command(label='保存',command=saveRecords)
mfile.add_command(label='另存为...',command=saveAsNew)
mfile.add_separator()
mfile.add_command(label='退出',command=root.destroy)
medit=Menu()
menuroot.add_cascade(label='编辑',menu=medit)#添加为级联菜单
medit.add_command(label='添加记录',command=newRecord)
medit.add_command(label='删除记录',command=delRecord)
medit.add_separator()
medit.add_command(label='计算总成绩',command=doSum)
medit.add_separator()
medit.add_command(label='设置比例',command=setOption)
root.mainloop()
