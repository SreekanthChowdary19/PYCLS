# WAP find all evens from the given list

x = [2, 3, 4, 5, 6, 91, 86, 15, 17]

evens = []
for e in x:
    if e % 2 == 0:
        evens.append(e)
print(evens)
