# WAP generate a list contains 10 4-digit random numbers 

# modularity ==> functions
import random

nums = []
for i in range(10):
    num = random.randrange(1000, 9999)
    nums.append(num)
print(nums)


evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
print(evens)

        
