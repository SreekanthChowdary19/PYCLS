# WAP print 10 random numbers

import random

import time


#num = random.randrange(100, 999)
#print(num)


i = 1

while i <=10:
    num = random.randrange(100, 999)
    print(num)
    time.sleep(3) # waits 3 sec

    i = i +1
