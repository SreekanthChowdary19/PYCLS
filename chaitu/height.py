#wap to accept the height of a person in centimeter and categorize the person according to their height

height=int(input("enter a height of a person in centimeter:"))
if height < 150:
    print("The person is :DWARF")
elif height >= 150 and height < 165:
    print(" The person is :AVERAGE HEIGHT")
elif height > 165:
    print(" The person is :TALL")
else:
    print(" thanku ")
