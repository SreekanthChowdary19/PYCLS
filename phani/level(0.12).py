#WAP TO CALCULATE PROFIT AND LOSS ON A TRANSACTION FROM THE GIVEN
#COST PRICE (CP) AND SELLING PRICE (SP)





cp=int(input("Enter the Cost Price:"))
sp=int(input("Enter the Selling Price:"))
if sp>cp:
    amount=sp-cp
    print("profit is made =rs",amount)
elif cp>sp:
    amount=cp-sp
    print("Loss is made == rs",amount)
else:
    amount= cp==sp
    print("there is no profit or loss")
