#wap to calculate and print the electricity bill
a=int(input("enter a customer id number:"))
print(a)
name="battula chaitanya"
print(name)
b=int(input("enter a units:"))
c=(b*1.20)
print(c,("there is a no current bill:"))
if b >=199  and b <=400:
    c1=b*1.50
    print(c1)
    print("this is your amout")
elif b >=400 and b <=600:
    c2=b*1.80
    print(c2)
    print("this is your amount:")
    
elif b >=600:
    c3=b*2
    print(c3)
    print("this is your amount:")
else:
    print("  ")
print("Thanku for customer")



