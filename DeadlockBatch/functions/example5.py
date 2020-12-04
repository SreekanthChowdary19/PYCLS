"""
WAP which is menu-driven program to compute the area of below shapes

1.  Circle  : Area : Pi * r * r
2.  Rectangle : Area : l * w
3.  Triangle : Area: 1/2 * base * height
"""

def circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

def rectangle_area(length, width):
    area = length * width
    return area

def triangle_area(base, height):
    area = (1/2) * (base * height)
    return area

def area():
    choise = int(input("ENtera choise (1: CIRCLE, 2: RECT, 3: TRIANGLE: )"))
    if choise == 1:
        r1 = 10
        ca = circle_area(r1)
        print("The area of cicle with radius : {} is {}".format(r1, ca))
    elif choise ==2:
        xl = 10
        yw = 20
        ra = rectangle_area(xl,  yw)
        print("The area of Rectal with dim: {} X {}  is {}".format(xl, yw, ra))
    elif choise ==3:
        base = 10
        ht = 20
        ta = triangle_area(base,  ht)
        print("The area of Triangle  with baseXHeight: {} X {}  is {}".format(base, ht, ta))
    else:
        print("In valid Choise")


area()
