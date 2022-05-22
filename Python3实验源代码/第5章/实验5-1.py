a=eval(input('请输入月收入（整数）：'))
b=eval(input('请输入社保金额（整数）：'))
c=eval(input('请输入专项扣除金额（整数）：'))
if type(a)!=type(1) or a<1:
    print('输入的不是有效收入')
elif type(b)!=type(1) or b<1:
    print('输入的不是有效社保金额')
elif type(c)!=type(1) or c<1:
    print('输入的不是有效专项扣除金额')
else:
    g=a-b-c-5000        #计算应纳税收入金额
    if g<=0:
        print('应缴税金额：0')
    elif g<=3000:
        print('应缴税金额：',g,'个税：',g*0.03)
    elif g<=12000:
        print('应缴税金额：',g,'个税：',g*0.1-210)
    elif g<=25000:
        print('应缴税金额：',g,'个税：',g*0.2-1410)
    elif g<=35000:
        print('应缴税金额：',g,'个税：',g*0.25-2660)
    elif g<=55000:
        print('应缴税金额：',g,'个税：',g*0.3-4410)
    elif g<=80000:
        print('应缴税金额：',g,'个税：',g*0.35-7160)
    else:
        print('应缴税金额：',g,'个税：',g*0.45-15160)
