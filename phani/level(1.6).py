#WAP TO PRINT ALL DUPLICATE VALUES IN DECENDING ORDER FROM THE GIVEN INPUT LIST
#INPUT_LIST=[401,403,409,403,453,402,438,401,444]



input_list=[401,403,409,403,453,402,438,401,444]
p=[]
g=[]
for ele in input_list:
    if ele not in p:
        p.append(ele)
    else:
        g.append(ele)
print(g)
