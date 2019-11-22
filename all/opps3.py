"""
__init__ method is a speacil method , we can call it as  a constructor
As programmer we no need call explicitly at the time of object creation
the compiler will invoke this method

We can use init method to initilize object common attributes

For examples:

name, age, ht etc
"""

class Student:

     def __init__(self, name, age, ht):
          self.name = name
          self.age = age
          self.ht = ht
     
     def display(self):
          print("Name: {} Age: {} Roll No: {}".format(self.name, self.age, self.ht))

# Create the object
s1 = Student("Mahesh", 26, 5.6) 
s2 = Student("Suresh", 25, 5.4)
s1.display()
s2.display()
