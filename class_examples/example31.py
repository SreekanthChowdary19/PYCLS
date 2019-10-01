"""
Function Overloading:

Same function name but exepcting to take different params or different return value
Note: In python there is no function overloadibg

When you try to implement same function multiple times
the latest defined function will overides with previous defined function
"""

def add(x, y):
    return x+y


ret = add(10, 20)

print(f"Sum of two values: {ret}") # 30


def add(x, y, z):
    return x+y+z

ret2 = add(10, 20, 30)

print(f"Sum of three values: {ret2}") # 60


ret3 = add(100, 200)
print(f"Sum of two values: {ret3}") # 300

