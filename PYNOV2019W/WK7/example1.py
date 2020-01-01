# Object Oriented Programming : Designing 

"""
Write a program add two complex numbers

5+7j    real1 + img1
3+4j    real2 + img2


8+11j    real1+real2 + img1+ img2

r1 = 5
i1 = 7

r2 = 3
i2 = 4

print(str(r1+r2)+ " + " +str(i1+i2) + "j" )

"""

# Object : Representing a multiple enties as a single entity or simply its a real entity
# Class : Its just template , representing object properties or simply its a logical entity

"""

Object (Person): Propeties

Attributes (Name, age, ht)  ==> string, age ==> int, ht ==> float

The attributes of a person object we are defining with Data types data memebers

Behaviours (listen() walk() talk())

   member functions
"""


# How to define a class?

"""

We can define a class with "class" keyword

SYNATX:


class <class_name>:
    # Attributes of an object
    # Behvaiours of an object

To access the class members we have to use object of that class
"""
# How to create object of a class
"""
We can create a object of a class using class name
"""


class Student:

    def display():
        print("Inside display method")





#display() # NameError: name 'display' is not defined




s1 = Student()
print(s1)
s1.display()  # TypeError: display() takes 0 positional arguments but 1 was given














