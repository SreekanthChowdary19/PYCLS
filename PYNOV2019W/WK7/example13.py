# MRO ==> Method Resolution Order

class A:

    def go(self):
        print("Go A go!")

    def ready(self):
        print("Stop A ready")

    def stop(self):
        print("Stop A stop")


class B:
    def go(self):
        print("Go B go!")

    def ready(self):
        print("Stop B ready")


class C(B, A):

    def go(self):
        print("Go C go!")


c1 = C()

c1.go()

c1.ready()
