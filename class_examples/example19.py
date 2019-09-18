# What happens if we have multiple conditions , and at  a time one condition
#needs to be run?

"""
if -elif ladder


SYNATX

if cond1:
   st1
elif cond2:
   st2
elif cond3:
   st3
:
:
:
else:
   stn # Optinal block
"""

# Note: There is no realation between number of conditions and number inputs
signal = input("Enter signal value: (1-red ,2-yellow, 3-Green):")
"""
if signal == '1':
    print("Please stop!")
elif signal == '2':
    print("Please Ready!")
else:
    print("Please Go!")
"""
if signal == '1':
    print("Please stop!")
elif signal == '2':
    print("Please Ready!")
elif signal == '3':
    print("Please Go!")
else:
    print("Invalid signal")










