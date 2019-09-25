# WAP print all the numbers from the given random list of 50 numbers from
# 1 to 1000
# and display all the numbers except the numbers which are divisible by 4 or 5



import random

rand_nums = []
for i in range(1, 51):
    num = random.randrange(1, 1000)
    rand_nums.append(num)
print(f"Toatl Rand nums: {len(rand_nums)}")
print(f"Rand nums: {rand_nums}")

output = []
for e in rand_nums:
    if e % 4 == 0 or e % 5 == 0:
        continue
    output.append(e)
print(f"Final output: {output}")

