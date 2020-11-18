a=[]
for ele in range(0,10):
    b=input("enter  the srting:")
    a.append(b)
c=[]
for ele1 in a:
    if len(ele1)%2 != 0:
        c.append(ele1)
print(c)
