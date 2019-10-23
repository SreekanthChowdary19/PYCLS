# WAP add two numbers

"""
Function overloading


Defining same function name multiple times with differant params and return values

In python no function overloaidng support

When you are trying to define same function multiple times , the previous defined function
overrides with latest function definition
"""

def add(x, y):
    return x+y


print(add(10, 20)) # 30


def add(x, y, z):
    return x+y+z

print(add(10, 20, 30)) # 60

print(add(100, 200)) # Error


