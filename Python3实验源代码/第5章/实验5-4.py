import sys
import traceback
while True:
    a=eval(input('请输入第1个数据：'))
    b=eval(input('请输入第2个数据：'))
    if a==-9999 or b==-9999:
        break               #结束循环，从而结束程序运行
    try:
        print(a,'+',b,'=',a+b)
    except:
        x=sys.exc_info()
        print('异常类型：%s' % x[0].__name__)
        print('异常描述：%s' % x[1])
        print('堆栈跟踪信息:')
        traceback.print_tb(x[2])

