"""
tax

Given below are the latest income tax slabs applicable for financial year 2018-19 (assessment year 2019-20). These will be applicable for FY 2019-20 as well.

The basic exemption limit for an individual depends on their age and residential status.

According to age, resident individual taxpayers are divided into three categories:
1. Resident individuals below the age of 60 years
2. Resident senior citizens of age between 60 years and above but below 80 years
3. Resident super seniors above 80 yrs

Read more at:
//economictimes.indiatimes.com/articleshow/62751981.cms?from=mdr&utm_source=contentofinterest&utm_medium=text&utm_campaign=cppst

"""

def get_tax(gross, per):
     tax = gross * (per/100)
     return tax
    

# Take income from user

net_income = float(input("Enter a salary : "))

age = int(input("Enter age: "))


if age < 60:
     if net_income <= 250000:
          print("No tax")
     elif net_income > 250000 and net_income <= 500000:
          tax = net_income * (5/100)
          print("Tax: {}".format(tax))
     elif net_income > 500000 and net_income <= 1000000:
          tax = net_income * (20/100)
          print("Tax: {}".format(tax))
     elif net_income > 1000000:
          tax = net_income * (30/100)
          print("Tax: {}".format(tax))
elif age >=60 and age<80:
     pass
elif age >=80:
     pass
