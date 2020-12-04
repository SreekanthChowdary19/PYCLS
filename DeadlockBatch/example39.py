
# Write a program   get 1st four numbers from the given list which are divisible by 4 and 16

x = range(1, 101)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16........22, 23, 24......96, 97,...100]

c = 0
for ele in x:
    if ele % 4 == 0 and ele % 16 == 0:
        print(ele)
        c = c+1
        if c == 4:
            break
