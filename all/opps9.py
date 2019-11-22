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

class Rect:

     def __init__(self, xcor, ycor, h, w):
          self.x = xcor
          self.y = ycor
          self.h = h
          self.w = w

     def display(self):
          print("x: {} y: {} and w:{} h:{}".format(self.x, self.y, self.h, self.w))


r1 = Rect(10, 20, 30, 40)
r1.display()
