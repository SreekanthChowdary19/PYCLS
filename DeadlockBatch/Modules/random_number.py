# Generate random number

import random
"""
x = []
for i in range(10):
   num = random.randrange(100, 999)
   x.append(num)
print(x)
"""


i = 0
x = []
while i<=10:
    num = random.randrange(100, 999)
    x.append("GF-" + str(num))
    i = i+1

print(x)
