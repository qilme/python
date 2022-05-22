while True:
    a=eval(input('请输入一个整数：'))
    if type(a)!=type(1):
        print('输入错误，请重新输入。')
    else:
        if a==-1:
            break               #输入-1时，结束while循环
