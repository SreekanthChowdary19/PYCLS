#count = 0

class Student:

     count = 0  # class variable 

     def __init__(self, name, age, ht):
          self.Name = name
          self.AGE = age
          self.ht = ht
          Student.count = Student.count +1

     def display(self):
          print("Name: {} Age: {} Rno: {}".format(self.Name, self.AGE, self.ht))

     def get_toatal(self):
          print(Student.count)



s1 = Student("A", 12, 4)

s2 = Student("B", 13, 4.5)

s3 = Student("C", 14, 5)

s4 = Student("D", 15, 5.5)

#print(s1.count)
#print(Student.count)
          
s4.get_toatal()
