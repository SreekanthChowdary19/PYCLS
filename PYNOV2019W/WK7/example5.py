"""

__init__ is a special method python. We can call it as constructor

This method will be invoked by compiler at the time object creation
"""

class Student:

    def __init__(self):
        print("Inside init method")

    def display(self):
        print("Inside display method")



s1 = Student() # Object creation statement will be invoked __init__ method s1
s2 = Student() # Object creation statement will be invoked __init__ method s2
s3 = Student() # Object creation statement will be invoked __init__ method s3


s1.display()  # invokes dispaly method with object s1
s3.display()  # invokes display method with objecr s3
 
