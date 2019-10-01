# WAP convert given string from lower case to upper case


def myupper(input_str): # bangalore
    output = ""
    for ch in input_str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            ch = chr(ord(ch) - 32)
        #print(ch)
        output = output + ch
    return output
        
    
input_str = input("Please enter a string : ")
print(f"The input: {input_str}")
responce = myupper(input_str)
print(f"The output: {responce}")
