# WAP add two numbers and print result multiply with number 100

# Local variables
"""
The variables which we defined inside function 
are the local variable to that function. The local variables of a function 
we can not acccess outside of the function definition

When we are trying to access the interpreter throws an error "variable/object  name is not defined"
"""
"""
def add(x, y):
    c = x+y
    print(c)


add(10, 20)

#print(c*100) # c is not defined
"""
# Solution 1:  
"""
To access the values computed inside function defnition we have to return those values from the function
"""
def add(x, y):
    c = x+y
    return (c)

result = add(10, 20)  # add(10, 20) will replace with return valye of the add() function

print("Result : ", result)
print("Multiply with 100", result*100)

