from turtle import *
begin_poly()#①	
goto(-10,0)
goto(0,30)
goto(10,0)
end_poly()	
p=get_poly()
register_shape('mp',p)#②
shape('mp')
