# break and continue are the loop statemnets


# WAP print all numbers from the given list using while loop
"""
x = [10, 20, 30, 40, 7, 90, 80]


i = 0


while i < len(x):
    print(x[i])
    i = i+1
"""


# WAP print all numbers from the given list till the number 7 encounters


x = [10, 20, 30, 40, 7, 90, 80]

i = 0

while i< len(x): # i<7

    if x[i] == 7:
        print("Break the loop")
        break
    print(x[i])
    i = i+1
print("Loop outiside")




