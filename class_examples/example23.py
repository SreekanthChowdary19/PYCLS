# WAP find even numbers from the given random list of 10 elements


# random is module 
import random

# randrange is a function defined in random module
#randnum = random.randrange(100, 999)
#print(randnum)


rand_nums = []
for i in range(10):
    randnum = random.randrange(10, 500)
    rand_nums.append(randnum)
print(f"Rand nums: {rand_nums}")

evens = []
for num in rand_nums:
    if num % 2 == 0:
        evens.append(num)
print(f"Evens: {evens}")
        
