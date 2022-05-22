times=0    #用于统计移动次数
def hannuota(nlist,mfrom,mpass,mto):
    global times
    n=len(nlist)
    if n==1:
        times+=1
        print('%-4d' % times,nlist[0],':',mfrom,'--------->',mto)
    else:
        hannuota(nlist[:n-1],mfrom,mto,mpass)
        hannuota([nlist[-1]],mfrom,mpass,mto)
        hannuota(nlist[:n-1],mpass,mfrom,mto)  
c=int(input('请输入盘子数：'))
#初始化盘子，用列表表示。
p=[]
for n in range(c):          #p=['a','b','c'……]
    p.append(chr(97+n))
hannuota(p[:],'A','B','C')
