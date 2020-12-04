import time
x = [10, 20, 30, 40]

# Taking for - loop help to traverse/iterate/visit each and every element
# from the given list x

# IN this case for loop runs 4 times
print("Traverseing a List")
time.sleep(10) # waits 10 sec
for ele in x:
    print("Inside loop")
    print(ele)
    time.sleep(2)
print("Outside loop")


print("Traverseing a tuple")
time.sleep(10) # waits 10 sec

y = ("Hyderabad", "Chennai", "BANGALORE", "Trivendrum")
for city in y:
    print("Inside loop")
    print(city)
    time.sleep(2)
print("Outside loop")

print("Traverseing a STRING")
time.sleep(10) # waits 10 sec
str1 = "PYTHON"
for ch in str1:
    print("Inside loop")
    print(ch)
    time.sleep(2)
print("Outside loop")



