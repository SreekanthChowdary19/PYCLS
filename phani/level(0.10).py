#WAP TO CHECK WHETHER A CHARACTER IS AN ALPHABET ,DIGIT OR SPECCIAL CHARACTER




char=input("enter a character:")
if(char>='a' and char<='z') or (char>='A' and char<='z'):
    print("character is an alphabet")
elif (char>="0" and char<="9"):
    print("character is an digit")
else:
    print("it is a special character")
