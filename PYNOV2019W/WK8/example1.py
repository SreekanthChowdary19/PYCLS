# oops

# Polymorphsm , inhertance 
class Shape:


    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor

    def move(self):
        self.x = self.x + 100
        self.y = self.y+ 100


    def display(self):
        print("x: {} y: {}".format(self.x, self.y))


#s1 = Shape(10, 20)

#s1.display()
#s2 = Shape(100, 200)

class Rect(Shape):

    def __init__(self, xcor, ycor, length, width):
        #self.x = xcor
        #self.y = ycor
        Shape.__init__(self, xcor, ycor)
        self.w = width
        self.h = length

    def display(self):
        print("x: {} y: {} w: {} and h: {}".format(self.x, self.y, self.w, self.h))

r1 = Rect(10, 20, 30, 40)
r1.display()

r1.move()
r1.display()

 


