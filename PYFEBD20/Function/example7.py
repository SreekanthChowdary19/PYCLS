"""
1- Defining a function and deecide the args
2- Function calling
3- Importance of the return statememnt 
"""


# WAP convert given string from lower case to upper case


def myupper(str_input):  # bangalore
    output = ""
    for ch in str_input:
         ch = chr(ord(ch) - 32)
         #print(ch)
         output = output + ch
    return output
         


result = myupper("bangalore")
print(result)
