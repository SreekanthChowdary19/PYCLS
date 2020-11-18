#WAP FIND ALL EVEN NUMBERS FROM THE GIVEN INPUT LIST AND DISPLAY OUTPUT AS A LIST
#FORMAT


p=[1,2,3,4,5,6,7,8,9,10,11,12]
g=[]
for ele in p:
    if ele%2==0:
        g.append(ele)
print(g)
