from random import *#①
cf='+-*/'
for n in range(10):
  a=randint(10,99)
  b=randint(10,99)
  c=sample(cf,1)[0]#②
  print(a,c,b)
