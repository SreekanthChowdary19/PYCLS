# WAP add two numbers and multiply result with 100


def add(x, y):
    c = x+y
    print(c)


add(10, 20)

print(c*100) # NameError: name 'c' is not defined


"""
The variables which we have defined insdie function definition

are the local variables to that function.
So we are not suppose to access outside of the function definition


If we are trying to access to outside we will get an error "name not defined"
"""
