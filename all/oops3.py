"""
OOPS PRinicples

Abstraction
Polymorphism
Encapsulation
Inheritance  ==> Parant and child 
"""

class Shape:

     def __init__(self, xcor, ycor):
          self.x = xcor
          self.y = ycor

     def move(self):
          self.x = self.x+100
          self.y = self.y+100

     def display(self):
          print("x: {} and y: {}".format(self.x, self.y))


#s1 = Shape(10, 20)

#s1.display()

class Rect(Shape): # Shape is base class we are inherited inside Rect class

     def __init__(self, xcor, ycor, h, w):
          #self.x = xcor
          #self.y = ycor
          Shape.__init__(self, xcor, ycor)
          self.h = h
          self.w = w

     def display(self):
          print("x: {} y: {} and w:{} h:{}".format(self.x, self.y, self.h, self.w))


r1 = Rect(10, 20, 30, 40)
r1.display()
r1.move()
r1.display()


