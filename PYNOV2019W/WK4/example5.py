#
"""

import os
cmd = 'ipconfig'


r = os.system(cmd)
if r == 0:
   print("Command executed success")
else:
   print("Fail to excute command")
"""


import os


def runCommand(cmd):
    r = os.system(cmd)
    if r == 0:
       return True
    else:
       return False


res = runCommand("ipconfig")
print(res)
#if runCommand("ipconfig"):
#   print("Do other stuff")
