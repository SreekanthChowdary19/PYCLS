#wap a coordinate point in a x y coordinate system and determine in which quadrant the
#coordinate point lies
x=int(input("enter a x-value:"))
y=int(input("enter a y-value:"))

if (x<=5 and x>0) and (y<=5 and y>0):
    print(" x,y are a 1st quadrant coordinate:")
elif( x<=-5 and x>-1)  or (y<=5 and y>0):
    print(" x,y are a 2nd quadrant coordinate:")
elif (x<0) and (y<0):
    print(" x,y are a 3rd quadrant coordinate:")
elif (x<=5 and x>0) or (y<=-5 and y>=-1):
    print(" x,y are a 4th quadrant coordinate:")
else:
    ("x,y values any quadrant coordinate:")
    
