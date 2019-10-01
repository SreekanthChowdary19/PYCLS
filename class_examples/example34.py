
"""
def add2(x, y):
    return x+y

def add3(x, y, z):
    return x+y+z


print(add2(100, 200))


print(add3(100, 200, 300))
"""
# Default argumnets

def add(x, y, z=0):
    return x+y+z


print(f"Sum of two values: {add(10, 20)}")


print(f"Sum of two values: {add(10, 20, 30)}")


# Note:
"""
The default args should follows Non-default args

add(x, y, z=0)

add(x, y=0, z=0) # We should have more than one dafault arguments
add(x=0, y=0, z=0) # WE can have all default args



add(x=0, y, z) # SYNATX ERROR
"""












