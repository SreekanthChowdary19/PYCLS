# WAP convert given string from lower case to upper case


"""
if-else ==> Optimization
"""


def myupper(str_input): # bangalore
    output = ""
    for ch in str_input:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):  # >= 97 and <=122
            ch = chr(ord(ch)-32)
        output = output+ch
            
    return(output)


x = input("Enter a string: ")
resp = myupper(x)

print(resp)


"""
Function Definition
Function call
Retunr statement
"""
