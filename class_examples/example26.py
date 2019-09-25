# WAP print all the numbers from the given random list of 50 numbers from
# 1 to 1000
# and display all the numbers till the number 100 encounters



import random

rand_nums = []
for i in range(1, 51):
    num = random.randrange(1, 1000)
    rand_nums.append(num)
print(f"Toatl Rand nums: {len(rand_nums)}")
print(f"Rand nums: {rand_nums}")

# Adding 100 at the 25th position
rand_nums.insert(25, 100)

print("="*40)
print(f"Toatl Rand nums: {len(rand_nums)}")
print(f"Rand nums: {rand_nums}")

output = []
for e in rand_nums:
    if e == 100:
        break
    output.append(e)
print(f"Output: {output}")
