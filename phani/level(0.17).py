#WAP TO CHECK WHETHER A TRIANGLE IS EQUILATERAL OR ISOSCELES OR SCALENE TRIANGLES



x=int(input("enter the first side:"))
y=int(input("enter the second side:"))
z=int(input("enter the third side :"))
if x==y==z:
    print("EQUILATERAL TRIANGLE")
elif x==y or y==z or z==x:
    print("ISOSCELES TRIANGLE")

else:
    print("SCALENE TRIANGLE")


