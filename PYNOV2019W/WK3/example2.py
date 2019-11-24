# What happens if we have multiple condition , but at a time one condition
# needs to be run?


"""
if <cond1>:
    st1
elif <cond2>:
    st2
elif <cond3>
    st3
else:
    print("Optional")
"""
# Trafic signals, red, yellow, green


signal = input("Enter a signal(1-red, 2-yellow, 3-green):")

if signal == '1':
    print("Please stop!")
elif signal == '2':
    print("Please alert!")
elif signal == '3':
    print("Please go")
else:
    print("In valid signal")
