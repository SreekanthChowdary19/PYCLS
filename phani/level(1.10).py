#WAP JOIN EACH AND EVERY CHARACTER FROM THE GIVEN STRING WITH HYPHEN(-)
#INPUT_STR="PYTHON"




"""input_str="PYTHON"
s='P'+"-"+'Y'+"-"+'T'+"-"+'H'+"-"+'O'+"-"+'N'
print(s)
"""




Input_str="PYTHON"
O=''
for i in range(len(Input_str)):
    if i!=len(Input_str)-1:
        O+=Input_str[i]+'-'
    else:
        O+=Input_str[i]
print(O)
