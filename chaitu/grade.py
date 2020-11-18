#wap to accept a grade and delclare the equialent description
a=int(input("enter your  marks:"))
E=a
V=a
G=a
A=a
F=a
if E >= 90 and E<=100:
    print("Excellent :grade is E")
elif V >= 80 and V<=90:
    print(" Very good:grade is V")
elif G >=60 and G<=80:
    print("Good")
elif A >= 35 and A<=60:
    print("Average")
elif F<=34:
    print(" Fail")
else:
    print(" invalid marks :max marks is 100 ")
    
