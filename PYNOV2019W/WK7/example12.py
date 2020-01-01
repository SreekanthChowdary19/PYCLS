class A:

    def go(self):
        print("Go A go!")

    def ready(self):
        print("Stop A stop")

    def stop(self):
        print("Stop A stop")


class B(A):
    def go(self):
        print("Go B go!")

    def ready(self):
        print("Stop B ready")

class C(B):
    def go(self):
        print("Go C go!")

class D(C):
    pass

c1 = D()
c1.go()
c1.ready()
c1.stop()

