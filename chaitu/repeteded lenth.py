#wap replace each string from the givrn list with the same string which is repeated with length of the string
x=["A" , "AB" , "ABC" , "ABCD"]
a=[]
for i in x:
    a.append(i*len(i))
print(a) 




