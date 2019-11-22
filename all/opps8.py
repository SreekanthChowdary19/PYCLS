
class Student:

     count = 0  # class variable 

     def __init__(self, name, age, ht):
          self.Name = name
          self.AGE = age
          self.ht = ht
          Student.count = Student.count +1

     def display(self):
          print("Name: {} Age: {} Rno: {}".format(self.Name, self.AGE, self.ht))

     @classmethod
     def get_toatal(cls):
          print(Student.count)


s1 = Student("A", 25, 5.4)  # display   get_total
s2 = Student("B", 26, 5.6)  # disply     get_total

Student.get_toatal()


# Instansce variable vs Class Variables
# Instance methods vs class methods
