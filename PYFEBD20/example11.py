# Write a program get all integer numbers from the given list


x = [10, 20, 30.5, "xyz", 50, "abcd", 19.5, [10, 20], 46]

print("Input: ", x)
y = []
for e in x:
    if type(e) == int:
        y.append(e)

print("Output: ", y)
