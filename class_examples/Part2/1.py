# WAP print all all even numbers from the given list
# and display output as a list


x = [10, 18, 19, 17, 16, 6, 5]

y = []
for e in x:
    if e % 2 == 0:
        y.append(e)
print(y)

#[10, 18, 16, 6]
