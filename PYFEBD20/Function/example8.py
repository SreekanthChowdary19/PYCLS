
def myupper(str_input):  # bangalore
    output = ""
    for ch in str_input:
         ch = chr(ord(ch) - 32)
         #print(ch)
         output = output + ch
    return output
         

x = input("Enter a string: ")
print("Input : ", x)
result = myupper(x)
print("Output: ", result)
