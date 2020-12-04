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

r1 = 10
ca = circle_area(r1)


xl = 10
yw = 20

ra = rectangle_area(xl,  yw)

base = xl
ht = yw
ta = triangle_area(base,  ht)


# format() is a string function can be used to format the string output
print("The area of cicle with radius : {} is {}".format(r1, ca))
print("The area of Rectal with dim: {} X {}  is {}".format(xl, yw, ra))
print("The area of Triangle  with baseXHeight: {} X {}  is {}".format(base, ht, ta))
