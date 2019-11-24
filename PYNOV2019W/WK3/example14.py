# WAP convert given string from lower case to upper case


def myupper(str_input): # bangalore
    output = ""
    for ch in str_input:
        ch = chr(ord(ch)-32)
        output = output+ch
    return(output)


resp = myupper("bangalore")

print(resp)
