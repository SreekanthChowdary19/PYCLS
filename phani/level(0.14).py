#WAP TO FIND THE ELIGIBILITY OF ADDMMISSION FOR A PERSONAL COURSE BASED ON THE
# FFOLLOWING CRITERIA
 


maths=int(input("enter the maths marks:"))
phy=int(input("enter the phy marks:"))
chem=int(input("enter the chem marks:"))
t=maths+phy+chem
mp=maths+phy
if (maths>=65) and (phy>=55)and (chem>=50)and (t>=180) or (mp>=140):
    print(" candidate is eligible for Admission")
else:
    print("candidate is not eligible for Admissiion")
