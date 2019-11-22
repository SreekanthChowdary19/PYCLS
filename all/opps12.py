# MRO: Method Resolution Order


class A:

     def go(self):
          print("Go A go!")

     def ready(self):
          print("Ready A ready!")

     def stop(self):
          print("Stop A stop!")

class B:

     def go(self):
          print("Go B go!")

     def ready(self):
          print("Ready B ready!")

class C(A, B):
     def go(self):
          print("Go C go!")


c = C()
c.go()
c.ready()
c.stop()


          

