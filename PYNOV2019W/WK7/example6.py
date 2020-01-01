"""

__init__ is a special method python. We can call it as constructor

This method will be invoked by compiler at the time object creation

To initilize object common attributes
"""

class Student:

    def __init__(self, name, age, ht):
        self.Name = name
        self.age = age
        self.Ht = ht

    def display(self):
        print("Name: {} Age:{} Ht: {}".format(self.Name, self.age, self.Ht))



s1 = Student("Hareesh", 24, 5.4) # Object creation statement will be invoked __init__ method s1
s2 = Student("Mahesh", 25, 5.6) # Object creation statement will be invoked __init__ method s2
s3 = Student("Suresh", 26, 5.7) # Object creation statement will be invoked __init__ method s3


s1.display()  # invokes dispaly method with object s1
s3.display()  # invokes display method with objecr s3
 
