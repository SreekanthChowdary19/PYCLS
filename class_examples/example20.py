#  WAP find all even numbers from the given list
"""
x = [10, 19, 18, 17, 16, 15, 14, 13]

# Trversing each element
for e in x:
    # Checking element is even or not
    if e % 2 ==0:
        print(e)
"""


x = [10, 19, 18, 17, 16, 15, 14, 13]
print(f"Input: {x}")
y = []
# Trversing each element
for e in x:
    # Checking element is even or not
    if e % 2 ==0:
        y.append(e)
print(f"Output: {y}")
