"""
__init__ is a speacil method python. We can call it as a constructor

this method will invoke(call) at the compiler at the time object creation
"""

class Student:

     def __init__(self):
          print("Inside init method")

     def display(self):
          print("Inside display method")



# Object Creation


s1 = Student()# ==> invoke the __init__ method

s1.display()
"""
Inside init method
Inside display method
"""
