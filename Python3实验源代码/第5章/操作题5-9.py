for m in range(2000):   
   s=1
   for a in range(2,m):	#计算m的因子之和
      if m%a==0:
         s+=a
   #计算s的因子之和
   s2=1
   for a in range(2,s):
      if s%a==0:
         s2+=a
   if s2==m and m!=s:
      print((m,s))      #输出亲密数对
