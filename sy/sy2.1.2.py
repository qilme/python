cou = 0
# 异常处理
while True:
    try:
        s = eval(input("请输入学生的成绩\n"))
        while s not in range(101):
            s = eval(input("请输入正确的成绩哟：\n"))
        else:
            break
    except (NameError, TypeError, SyntaxError):
        cou += 1
        if cou >= 6:
            exit("哼(￢︿̫̿￢☆)，不跟你玩了")
        elif cou > 3:
            print("再捣蛋，我就生气啦啊ヽ（≧□≦）ノ")
        else:
            print("不要调皮导弹啊（；´д｀）ゞ")
# 成绩判断
if s >= 90:
    print("优秀")
elif s >= 80:
    print("良好")
elif s >= 60:
    print("及格")
elif s >= 0:
    print("不及格")
