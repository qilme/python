d={1:'one',2:'two',3:'three',4:'four',5:'five'}
a=int(input('请输入一个整数：'))
if a in d:
   b=d.pop(a)
   print('已从字典删除键值对：{%s:"%s"}'%(a,b))
else:
   print(a,'不是字典中的键')
