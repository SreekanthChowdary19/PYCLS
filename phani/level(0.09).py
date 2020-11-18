# WAP TO FIND THE LARGEST OF THREE NUMBERS



x=int(input("Enter the x value:"))
y=int(input("Enter the y value:"))
z=int(input("Enter the z value:"))
if x>y and x>z:
    print("the largest number is x")
elif y>x and y>z:
    print("the largest number is y")
else:
    print("the largest number is z")
