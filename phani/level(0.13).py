#WAP TO READ TEMPERATURE IN CENTIGRADE AND DISPLAY A SUITABLE MESSAGE ACCOURDING
# TO TEMPERATURE STATE BELOW




TEMP=int(input("enter the temperature:"))
if TEMP<0:
    print("freezing weather")
elif TEMP<10:
    print("very cold weather")
elif TEMP<20:
    print("freezing weather")
elif TEMP<30:
    print("temperature is normal")
elif TEMP<40:
    print("temperature is hot")
else:
    print("temperature is very hot")
