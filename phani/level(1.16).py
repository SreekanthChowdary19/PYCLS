#WAP FIND ALL THE EVEN NUMBERS FROM YHE GIVEN LIST.



input_list=[18.8,"Hyd",18,26.9,19,"BANG",26,33.7,25,"CHEN"]
for ele in input_list:
    if type(ele)==int and ele%2==0:
        print(ele)
