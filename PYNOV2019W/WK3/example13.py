# WAP add two numbers and multiply result with 100

"""
Using return statement we can access the values computed inside a function
to the outside of the function definition



"""

def add(x, y):
    c = x+y
    return c # Retunrs the value of c to the calling sattements


r = add(10, 20) # The function calling statement will replaces with return
                # value of teh function

print(r*100)

