
x=int(input("enter the x value:"))
y=int(input("enter the y value:"))
if x>0 and y>0:
    print("First Quadrant")
elif x<0 and y>0:
    print("Second Quadrant")
elif x<0 and y<0:
    print("Third Quadrant")
elif x>0 and y<0:
    print("Fourth quadrant")
else:
    print(" point lies on origin")
