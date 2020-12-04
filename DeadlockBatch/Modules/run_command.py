import os
#cmd = 'free -m'
cmd = input("Enter a comamnd: ")
resp = os.system(cmd)
"""
if resp == 0:
    print("="*50)
    print("Command executed successfully!")
    print("="*50)
else:
    print("="*50)
    print("Fail to execute command!")
    print("="*50)
"""
