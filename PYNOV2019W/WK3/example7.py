# WAP print all the numbers from the given random list except the number which are
# divisible by 4

# The continue statemnet will skip the iterations

x = [2, 9, 7, 8, 6, 4, 19, 12, 13]


i = 0


while i < len(x):
    if x[i] % 4 == 0:
        i = i+1
        continue
    print(x[i])
    i = i+1
