# WAP print sqaure of each and every elemenet from the given list

"""
x = [2, 4, 6, 8]

for ele in x:
    print(ele*ele)
"""


# WAP print sqaure of each and every elemenet from the given list and display
# output as a list

"""
x = [2, 4, 6, 8]

y = []  # Place holder to store the output

for e in x:
    y.append(e*e)
    #print(y) - debug

print(y)

"""


# WAP replace each value from the given list with square of respective number

x = [2, 4, 6, 8]

print("Input: ", x)

indexes_of_x = range(0, len(x))
"""
# Logic
x[0] = x[0] * x[0]
x[1] = x[1] * x[1]
x[2] = x[2] * x[2]
x[3] = x[3] * x[3]
"""
for i in indexes_of_x:
    #print(i)
    x[i] = x[i] * x[i]

    
print("Output: ", x) # []

for i in range(0, len(x)):
     x[i] = x[i] * x[i]








