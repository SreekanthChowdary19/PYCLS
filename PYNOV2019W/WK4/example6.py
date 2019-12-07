
import os


#res = os.system('net start')

#print(res)


import subprocess


response = subprocess.check_output(['net', 'start'])
#print(type(response))

response = response.decode("utf-8")
#print(type(response))
#print(response)

lines = response.split("\n")
#print(lines)

for line in lines:
     #print(type(line))
     line = line.strip()
     if line.startswith('McAfee'):
          print(line)
