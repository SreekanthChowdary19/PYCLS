

class Rect:

    def __init__(self, xcor, ycor, width, height):
        self.x = xcor
        self.y = ycor
        self.w = width
        self.h = height


    def display(self):
        print("x: {} y: {} h: {} w: {}".format(self.x, self.y, self.h, self.w))


r1 = Rect(10, 20, 30, 40)
r1.display()
