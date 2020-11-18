#wap to check a triangle is equilateral , isosceles or scalene
a=int(input("enter a angle:"))
b=int(input("enter b angle:"))
c=int(input("enter c angle:"))
if a==b==c:
    print("equilateral teiangle")
elif a==b or b==c or a==c:
    print("isosceles triangle:")
elif a!=b!=c:
    print("scalene triangle:")
else:
    print("thanku :")
