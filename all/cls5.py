"""
For same class we can create N- number of objects

If we create N-objects the init method will invoke N-times

The adavanatge of __init__ method is we can initilize object common attributes
"""

class Student:

     def __init__(self):
          print("Inside init method")

     def display(self):
          print("Inside display method")



# Object Creation

s1 = Student() # It will invoke __init__ method
s2 = Student() # It will invoke __init__ method
s3 = Student() # # It will invoke __init__ method


s1.display() # will invoke display method
s3.display() # will invole display method 
