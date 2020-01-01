class Shape:

    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor

    def move(self):
        self.x = self.x + 100
        self.y = self.y + 100

    def display(self):
        print(f"X: {self.x} and Y: {self.y}")


    
        
s1 = Shape(10, 20)
s2 = Shape(30, 40)
s1.display()  # 10 20
s2.display()  # 10 20 
s2.move()
s1.display()  # 10 20
s2.display()  # 110 120
