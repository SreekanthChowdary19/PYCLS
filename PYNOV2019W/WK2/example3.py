# Iterative statements(loops)

     #1. for - If you are working any sequnces directly we can use for loop
     #2. while*

# List + For  ==> Python Programmer

# SYNATX

"""
for <ele> in <seq>: # List, tuple, string, dict, any python seq object
    # Loop statemnets
"""


# Traversing a list

x = [10, 20, 30, 40]
print("Traversing a list: {}".format(x))

for e in x:
    print(e) # 10, 20, 30, 40

print("="*40)
# Traversing a string
str1 = "BANGALORE"
print("Traversing a string: {}".format(str1))

for ch in str1:
    print(ch)


print("="*40)
# Traversing a tuple
t = (100, 200, 300, 400)
print("Traversing a tuple: {}".format(t))
for ele in t:
    print(ele)

    
