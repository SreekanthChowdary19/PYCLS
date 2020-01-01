class Shape:

    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor

    def move(self):
        self.x = self.x + 100
        self.y = self.y + 100

    def display(self):
        print(f"X: {self.x} and Y: {self.y}")





class Rect(Shape): # We are inherited Shape class inside Rect class
    """
    Shape is a parent or base class
    Rect is a child or derived class
    """

    def __init__(self, xcor, ycor, width, height):
        #self.x = xcor
        #self.y = ycor
        Shape.__init__(self, xcor, ycor)
        self.w = width
        self.h = height


    def display(self):
        print("x: {} y: {} h: {} w: {}".format(self.x, self.y, self.h, self.w))


r1 = Rect(10, 20, 30, 40)
r1.display()

