"""
self represents currenr class objects

used to differentiate on which object we are invoking a class members
"""

class Customer:

    def display_customer_info(self):
        print("Inside display method: {}".format(self))





#display() # NameError: name 'display' is not defined




c1 = Customer()

c2 = Customer()

c3 = Customer()

#TypeError: display_customer_info() takes 0 positional arguments but 1 was given

print(c1)
c1.display_customer_info() # display_customer_info(c1)
print("="*30)

print(c2)
c2.display_customer_info() # display_customer_info(c2)

print("="*30)
print(c3)
c3.display_customer_info() # display_customer_info(c3)


