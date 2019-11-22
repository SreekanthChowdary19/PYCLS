count = 0

class Student:

     def __init__(self, name, age, ht):
          global count
          self.Name = name
          self.AGE = age
          self.ht = ht
          count = count +1

     def display(self):
          print("Name: {} Age: {} Rno: {}".format(self.Name, self.AGE, self.ht))

     def get_toatal(self):
          print(count)



s1 = Student("A", 12, 4)

s2 = Student("B", 13, 4.5)

s3 = Student("C", 14, 5)

s4 = Student("D", 15, 5.5)

s1.get_toatal()
          
