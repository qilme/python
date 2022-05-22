import time
begin=time.monotonic()
while True:
    print(time.strftime('%Y-%m-%d %H:%M:%S') ,end='')
    time.sleep(1)
    print('\r',end='')
    end=time.monotonic()
    if end-begin>60:        #程序运行时间超过1分钟则跳出循环，结束程序
        break;
