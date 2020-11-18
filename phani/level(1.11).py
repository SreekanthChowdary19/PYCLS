a=[]
for ele in range(0,10):
    s=input(" enter the string:")
    a.append(s)
b=[]
for ch in a:
    if len(ch)%2!=0:
        b.append(ch)
print(b)
        
        
