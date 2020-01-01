
class Student:

    def display(self):
        print("Inside display method")





#display() # NameError: name 'display' is not defined




s1 = Student()
print(s1)
s1.display()  # TypeError: display() takes 0 positional arguments but 1 was given


