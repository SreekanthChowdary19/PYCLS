def add(x, y):
    return x+y

def sub(x, y):
    return abs(x-y)

def mul(x, y):
    return x*y

def div(x, y):
    try:
        return x//str(y)
    except ZeroDivisionError:
        print("Please enter seocnd value as non-zero value")
    except Exception  as e:
        print("Some other error: "+ str(e))


a = int(input("Enter 1st value: "))
b = int(input("Enter 2ed value: "))

user_choise = input("Enter (1-add 2-sub 3-mul 4-div):")

if user_choise == '1':
    print(add(a, b))
elif user_choise == '2':
    print(sub(a, b))
elif user_choise == '3':
    print(mul(a, b))
elif user_choise == '4':
    print(div(a, b))
else:
    print("Invalid ibnput")
