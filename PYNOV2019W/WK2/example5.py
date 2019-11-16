# WAP find sum of all the elemnts from 1 to 5



# Defining elemnts from 1 to 5

x = range(1, 6)

s = 0  # Its place holder to store the output
# Traversing each element from given seq

for val in x: # [1, 2, 3, 4, 5]
     s = s+val
     #print(s)

print("Outside of for loop")
print(s)

"""                s        val    final s
Iteration 1 ==>    0         1         0+1 = 1
Iteration 2 ==>    1         2        1+2 = 3
Iteration 3 ==>    3        3         3+3 = 6
Iteration 4===>    6        4         6+4 = 10
Iteartion 5 ==>    10       5         10 + 5 = 15
"""
