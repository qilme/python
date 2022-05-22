"""
实现功能：
1. 输错三次自动纠错
2. 输入错误提醒
3. 轮数设定（不完善，仅首轮）
4. 作答时间显示
未实现功能：
1. 图形界面UI
2. 娱乐性
3. 代码复用
"""
import random
import time
# 基本参数设置
cou, cou1, cou2, cou3, cou4, cou5 = 0, 0, 0, 0, 0, 0
If = 1
# 话术本
res = ["答对了哟ヾ(≧▽≦*)", "干巴爹┗|｀O′|┛ 嗷~~", "继续加油(ง •_•)ง", "哦豁霍，不错不错"]
res1 = ["答错了诶(～￣▽￣)～", "敲脑阔哟了( ´･･)ﾉ(._.`)", "不对不对┑(￣Д ￣)┍"]

while True:
    try:
        ll = int(input("请选择难度：\n普通（2）简单（1）\n"))
        while ll not in {1, 2}:
            ll = int(input("请输入正确的难度等级哟：\n"))
        else:
            break
    except ValueError:
        cou5 += 1
        if cou5 >= 6:
            exit("哼(￢︿̫̿￢☆)，不跟你玩了")
        elif cou5 > 3:
            print("再捣蛋，我就生气啦啊ヽ（≧□≦）ノ")
        else:
            print("不要调皮导弹啊（；´д｀）ゞ")
# 轮数设定
while True:
    try:
        uco = int(input("请问要玩几轮？\n"))
        if uco == 0:
            print("所以说是玩还是不玩捏( •̀ ω •́ )y")
            continue
        else:
            break
    except ValueError:
        cou4 += 1
        if cou4 >= 6:
            exit("哼(￢︿̫̿￢☆)，不跟你玩了")
        elif cou4 > 3:
            print("再捣蛋，我就生气啦啊ヽ（≧□≦）ノ")
        else:
            print("不要调皮导弹啊（；´д｀）ゞ")

# 以下：判断对错 + 错误纠正


def TF():
    global uas, tas, t2, t1, show, cou1, cou2, If, uco
    if uas == tas:
        print(random.choice(res) + "\n本题用时{:.2f}秒。".format(t2 - t1))
        cou1 += 1
        if cou1 == uco:
            If = int(input("你已经玩了{}轮了，还要继续吗？\n玩的话扣1，不玩输0：\n".format(cou1)))
    elif uas == 0:
        If = uas
    else:
        uas = int(input(random.choice(res1) + "\n" + show))
        cou2 += 1
        if cou2 < 2:
            TF()
        else:
            print("正确答案是{}，下次加油吧！".format(tas))
            cou2 = 0


print("Tips:按0随时可以退出。")
# 主功能：随机数字生成 + 难度参数设定 + 用户答案输入
while If == 1:
    l11 = random.randint(1, 9)
    l12 = random.randint(1, 9)
    l21 = random.randint(10, 99)
    l22 = random.randint(10, 99)
    tas1 = l11 + l12
    tas2 = l21 + l22
    show1 = "{}+{}=".format(l11, l12)
    show2 = "{}+{}=".format(l21, l22)
    try:
        if ll == 1:
            tas = tas1
            show = show1
        elif ll == 2:
            tas = tas2
            show = show2
        t1 = time.time()
        uas = int(input(show))
        t2 = time.time()
        TF()

    except ValueError:
        cou3 += 1
        if cou3 >= 6:
            exit("哼(￢︿̫̿￢☆)，不跟你玩了")
        elif cou3 > 3:
            print("再捣蛋，我就生气啦啊ヽ（≧□≦）ノ")
        else:
            print("不要调皮导弹啊（；´д｀）ゞ")
# 结束语
else:
    print("下次也要来玩哟(＾Ｕ＾)ノ~ＹＯ")
