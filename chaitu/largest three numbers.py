#wap to find the largest of three numbers
x=int(input("enter a 1st value :"))
x1=int(input("enter a 2nd value :"))
x2=int(input("enter a 3rd value :"))
if x>x1 and x>x2:
    print("1st is max value:")
elif x1>x and x1>x2:
    print("2nd is max  value:")
elif x2>x and x2>x1:
    print("3rd is max value:")
else:
    print("invalid value of user:")
