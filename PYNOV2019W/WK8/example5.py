#count = 0

"""
Instance variable vs Class variable
AVoid the global variables

insatncce method vs class method vs static method

__str__ method 

"""

class Student:

    count = 0
    
    def __init__(self, name, age):
        self.Name = name
        self.age = age
        #global count
        Student.count = Student.count +1

    def display(self):
        print("Name: {}".format(self.Name, self.age))

    # to string method
    def __str__(self):
        return self.Name

    @classmethod  # In-built decorator
    def get_total(cls):
        print(cls.count)  # Name

    @staticmethod
    def avg(x):
        return sum(x)/len(x)
        



s1 = Student("Hareesh", 24)

s2 = Student("Hareesh2", 25)
s3 = Student("Hareesh3", 26)
s4 = Student("Hareesh4", 27)

print(Student.avg([10, 20]))
print(s4.avg([40, 50]))

