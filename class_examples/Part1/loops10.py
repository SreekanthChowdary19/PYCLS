# WAP replace each elment from the given list with square of
# the respctive number


x = [2, 4, 6, 8]
"""
print("Input", x)
x[0] = x[0] * x[0]
x[1] = x[1] * x[1]
x[2] = x[2] * x[2]
x[3] = x[3] * x[3]

print("Output", x)
"""
import time 
for i in range(0, len(x)): # range(0, 4) ==> [0, 1, 2, 3]
    print(i, x[i])
    time.sleep(4)
    x[i] = x[i] * x[i]
    print(x)
