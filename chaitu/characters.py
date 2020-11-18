#wap to check whether a character is an alphabet,digit or sp character
a=input("enter a any character :")
if a>='a' and a<='z':
    print("small letters character:")
elif a>='A' and a<='Z':
    print(" capital letters characters:")
elif a>='0' and a<='9':
    print("this is a digits:")
else:
    print("this is a special character:")
