"""
if - elif ladder


if cond1:
   # st1
elif cond2:
   # st2
elif cond3:
   # st4
:
:
:
elif condn:
   # stn
else:
   # optional block 
"""


# trafic signals 3 signals ==> 1 signals 


signal = input("Enter siganl (1-red 2-yellow 3-green): ")

if signal == '1':
    print("Please stop")
elif signal == '2':
    print("Please Ready!")
elif signal == '3':
    print("Please GO!")
else:
    print("Invalid signal")
