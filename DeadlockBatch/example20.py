# Mutability Objects(We can change) ---> List
#vs Immutable Objects (We can not change) --> Strings, Tuple etc


# WAP replace each value from the
# given list with square of respective number

x = [2, 4, 6, 8]

print("Input, ", x)
"""
x[0] = x[0] * x[0]
x[1] = x[1] * x[1]
x[2] = x[2] * x[2]
x[3] = x[3] * x[3]
"""
for i in range(0, len(x)):  # for i in [0, 1, 2, 3]:
    x[i] = x[i] * x[i]
    
    
print("Output", x)
