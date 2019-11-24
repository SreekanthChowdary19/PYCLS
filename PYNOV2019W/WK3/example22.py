# Default arguments
"""
When you define a default values to the function args

when the user is not passing any values , it will consider default value

If user pass value the default value will updated with user passed value

"""
# x, y are the Non-default args
# z is deafult arg

def add(x, y, z=0):
    c = x+y+z
    return c

#print(add(10, 20))

print(add(10, 20, 30))

# Note: The default args should follows Non-default args

"""
x=0, y=0, z=0 valid
x=0, y, z Not valid

x , y=0, z=0 valid

x, y=0, z In valid
"""
