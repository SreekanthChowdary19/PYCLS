# WAP TO READ ANY MONTH NUMBER IN INTEGER AND DISPLAY THE NO.OF DAYS FOR THAT MONTH

month_number=int(input("enter the month number:"))
if (month_number==1 or 3 or 5 or 7 or 8 or 10 or 12):
    print(" this month has 31 days")
elif month_number==2:
    print(" this month has 28 days")
elif (month_number==4 or 6 or 9 or 11):
    print("this month has 30 days")
else:
    print("invalid month number")

