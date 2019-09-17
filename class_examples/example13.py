# WAP replace each element from the given list with square of resctive number

x = [2, 4, 6, 8]
print(f"Input : {x}")

# Logic
"""
x[0] = x[0] * x[0]
x[1] = x[1] * x[1]
x[2] = x[2] * x[2]
x[3] = x[3] * x[3]
"""
for index in range(0, len(x)) :
    #print(index)
    x[index] = x[index] * x[index]
print(f"Output Modified Input list : {x}")
