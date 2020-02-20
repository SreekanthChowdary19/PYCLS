# WAP add two numbers and multiply result with 100
"""
By using return statement we can get the values computed inside
function to the outside of the function definition

returning a value from the function is an optional
By default return value is None

Collecting a return value is also an optional

Function calling statemnet will replace with return value of the function
"""
def add(x, y):
    c = x+y
    return c


r = add(10, 20)
print(r)
print(r*100)

r2 = add(100, 200)
print(r2)


#
print("=====")
add(1000, 20000)
