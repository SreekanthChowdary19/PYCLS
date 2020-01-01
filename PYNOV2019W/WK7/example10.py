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
        print("Stop B stop")


b1 = B()
b1.go()
b1.ready()
b1.stop()
