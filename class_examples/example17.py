# WAP print all the vowels from the list of strings


names = ["manohar", "anil", "suresh", "keswari"]


for name in names:
    print(f"Name: {name}")
    for ch in name: 
        #print(ch)
        if ch == 'e' or ch == 'a' \
           or ch == 'i' or ch == 'o' or ch == 'u':
            print(ch)
    print("="*40)
    

# Note : print() statement we can use to trace or debug the program or application
# flow
