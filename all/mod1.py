import os
import time




# system() function returns a 0 value once the command execution is success


response = os.system('ipconfig')
time.sleep(3) # waits 3 sec

if response == 0:
     print("Command executed successfully")
else:
     print("Fail to run the command")

     
