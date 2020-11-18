#wap to find the eligibility of admission for a professional course based on following criteria:
#marks in maths >_65
#marks in phy >=55
#marks in chem >=50
# total in all three subjects >=180
#or
#total in math and physics >140
maths=int(input("enter a maths marks is:"))
physics=int(input("enter a physics marks is:"))
chemestry=int(input("enter a chemestry marks is:"))
total=maths+physics+chemestry
mp=maths+physics
if maths >=65 and physics >=55 and chemestry >= 50 and total >=180 or mp >=180:
    print("the candidate eligibile for admission for a professional course:")
else:
    print("sorry you are not elegibile for admission for a professional course:")



