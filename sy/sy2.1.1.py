"""1.	输入一个学生的成绩，将其转化成简单描述：不及格（小于60）、及格（60-79），良好（80-89），优秀（90-100）。
要求:用两种方法完成，并且需要考虑输入数字不合法的情况。
提示：方法一用if结构完成，完成后的if语句可以任意交换书写行；
方法二用if……elif完成，注意分支之间的逻辑关系；
方法三用选择结构的嵌套完成if……else"""
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
if s in range(90, 101):
    print("优秀")
if s in range(80, 90):
    print("良好")
if s in range(60, 80):
    print("及格")
if s in range(0, 60):
    print("不及格")
