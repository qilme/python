def faver(a):#①
   s=0
   for n in a:
      s+=n
   return s/len(a)#②
(*a,)=eval(input('请输入逗号分隔的多个数据：'))
print('平均值=',faver(a))
