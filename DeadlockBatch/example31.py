# Write a program print  the charcters at the index position
#is divisible by 4


str1 = "PYTHON PROGRAMMING IS VERY EASY"

for i in range(0, len(str1)):
    if i % 4 == 0:
        print(i, str1[i])
