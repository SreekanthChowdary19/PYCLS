"""
Function overloading : Same function name in diffeent froms

In python no function overloading

When we define two functions with same name ,
the latest defined function will be overrides with previous defined function

"""


#  Write a program add two numbers


def add(x, y):
    c = x+y
    return c



print(add(10, 20)) # 30


# Write a program add three number

def add(x, y, z):
    c = x+y+z
    return c


print(add(10, 20, 30)) # 60

print(add(100, 200)) # 300 TypeError: add() missing 1 required positional argument: 'z'
