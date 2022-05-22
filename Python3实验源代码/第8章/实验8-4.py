from tkinter import *

root = Tk()
root.title('简单计算器')
root.geometry("400x300")
root.resizable(width=False, height=False)
frame1 = Frame(bd=2)
frame1.pack(anchor=N, fill=X)
sc = Scrollbar(frame1)
sc.pack(side=RIGHT, fill=Y)

text1 = Text(frame1)
text1.config(font=('宋体', 18, 'normal'))
text1.place(width=380)
sc.config(command=text1.yview)
frame2 = Frame(bd=2)
frame2.pack(anchor=CENTER, fill=BOTH)


def dow(event):
    obj = event.widget
    try:
        if event.widget['text'] == 'C':
            text1.delete('1.0', END)
        elif event.widget['text'] == '=':
            exp = text1.get('1.0', END)
            x = eval(exp)
            text1.insert(INSERT, '=' + str(x))
        else:
            text1.insert(INSERT, event.widget['text'])
    except:
        text1.insert(INSERT, '：表达式错误')


bts = [[], [], [], []]
f = ('宋体', 16, 'normal')
for n in range(1, 5):
    bts[0].append(Button(frame2, text=str(n), anchor=CENTER, font=f, width=8, height=2))
    bts[0][n - 1].grid(row=0, column=n - 1)
    bts[0][n - 1].bind('<Button-1>', dow)
for n in range(5, 9):
    bts[1].append(Button(frame2, text=str(n), anchor=CENTER, font=f, width=8, height=2))
    bts[1][n - 5].grid(row=1, column=n - 5)
    bts[1][n - 5].bind('<Button-1>', dow)
cf = ['9', '0', '+', '-']
for n in range(4):
    bts[2].append(Button(frame2, text=cf[n], anchor=CENTER, font=f, width=8, height=2))
    bts[2][n].grid(row=2, column=n)
    bts[2][n].bind('<Button-1>', dow)
cf = ['*', '/', 'C', '=']
for n in range(4):
    bts[3].append(Button(frame2, text=cf[n], anchor=CENTER, font=f, width=8, height=2))
    bts[3][n].grid(row=3, column=n)
    bts[3][n].bind('<Button-1>', dow)
