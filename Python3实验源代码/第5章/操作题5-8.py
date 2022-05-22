for n in range(100,1000):
   a=n//100			#获得百位上的数字
   b=n%100//10			#获得十位上的数字
   c=n%10			#获得个位上的数字
   if a*a*a+b*b*b+c*c*c==n:
      print(n)
