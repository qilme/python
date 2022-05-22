"""
如果整数m的全部因子（包括1，不包括m本身）之和等于n;
且整数n的全部因子（包括1，不包括n本身）之和等于m,则将整数m和n称为亲密数。
输入2000以内的全部亲密数
"""


def judge(m):
    n = 0
    factors = []
    # 通过取余来判断是否为因子，并将因子添加到列表
    for a in range(1, m):
        if m % a == 0:
            factors.append(a)
    for b in factors:
        n += b
    if n == m:
        print(m)


for c in range(1, 2001):
    judge(c)
