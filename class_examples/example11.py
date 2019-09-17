# WAP find find square each and every element from the given list
# and display the output in list format

import time
x = [2, 4, 6, 9]

y = [] # Place holder to store the output
print(f"Input: {x}")

for e in x:
    #time.sleep(3)
    y.append(e*e)
    #print(e, y)
print(y)
