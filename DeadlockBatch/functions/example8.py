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

def area(choise, *args):
    import sys
    if not len(args) <= 2:
        # exit the program
        print("Not valid input : {}".format(args))
        sys.exit(0)
    if choise == 1:
        ca = circle_area(args[0])
        print("The area of cicle with radius : {} is {}".format(args, ca))
    elif choise ==2:
        ra = rectangle_area(args[0],  args[1])
        print("The area of Rectal with dim: {} X {}  is {}".format(args[0], args[1], ra))
    elif choise ==3:
        ta = triangle_area(args[0], args[1])
        print("The area of Triangle  with baseXHeight: {} X {}  is {}".format(args[0], args[1], ta))
    else:
        print("In valid Choise")


area(1, 10)
area(2, 10, 20)
area(2, 100, 20)
area(3, 10, 20)


area(2,20, 30, 40, 50)



