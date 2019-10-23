# Default arguments

"""
def add2(x, y):
    return x+y

def add3(x, y, z):
    return x+y+z

"""


def add(x, y, z=0):
    return x+y+z


print(add(10, 20))
print(add(10, 20, 30))


# Rule to define a default args

"""
For user defined functions the default args should follow non-default args


# valid
def add(x, y, z=0):
    return x+y+z

# Not valid
def add(x, y=0, z):
    return x+y+z

# valid
def add(x, y=0, z=0):
    return x+y+z

#valid
def add(x=0, y=0, z=0):
    return x+y+z

"""








