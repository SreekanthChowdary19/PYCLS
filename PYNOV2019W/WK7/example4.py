"""

__init__ is a special method python. We can call it as constructor

This method will be invoked by compiler at the time object creation
"""

class Student:

    def __init__(self):
        print("Inside init method")

    def display(self):
        print("Inside display method")


s1 = Student() # Created an object 
s1.display() # Calling a function
