class Shape:

     def __init__(self, xcor, ycor):
          self.x = xcor
           self.y = ycor
     """
     def display(self):
          print("x: {} and y: {}".format(self.x, self.y))
     """
     
     def __str__(self):
         return ("x: {} and y: {}".format(self.x, self.y))

s1 = Shape(10, 20)

#s1.display()

#print(dir(s1))

print(s1) # Genrally it s printing address of an object

# But instaed of address we need to print state of the object
