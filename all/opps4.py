"""
self param basically it iis going differentiate on which object you are invokeing
function/method/data
"""

class Student:
     """
     def __init__(self, name, age, ht):
          self.name = name
          self.age = age
          self.ht = ht
     """
     def display(self):
          print("studnet information")

# Create the object

s1 = Student() # it invokes the init method
s2 = Student()

s1.display() # display(s1)
s2.display() # display(s2)

# One display ==> s1 and s2
