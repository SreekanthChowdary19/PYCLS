# WAP find square of each element from the given lsit



x = [2, 4, 6, 8]

for e in x:
   print(e*e)
print("="*50)

# WAP find square of each element from the given lsit and display output
# as list

x = [2, 4, 6, 8]
y = [] # Place holder to display the output
for e in x:
     y.append(e*e)
     #print(y)
print(y)

print("="*50)
# WAP replace each value in a list with square of respctive number
x = [2, 4, 6, 8]
print("Input: {}".format(x))
# Logic
"""
x[0] = x[0] * x[0]
x[1] = x[1] * x[1]
x[2] = x[2] * x[2]
x[3] = x[3] * x[3]
"""
indexes = range(0, len(x))
for i in indexes:
     #print(i)
     x[i] = x[i] *x[i]
print("Output: {}".format(x))

"""
for i in range(0, len(x)):
     #print(i)
     x[i] = x[i] *x[i]
print("Output: {}".format(x))
"""

