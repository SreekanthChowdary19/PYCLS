class A:

     def go(self):
          print("Go A go!")


class B(A):

     def go(self):
          print("Go B go!")

     def ready(self):
          print("Ready B ready!")





a = A()
a.go()
a.ready() # Error : Parent class , is not suppose to access child class
# methods or attributes



          

