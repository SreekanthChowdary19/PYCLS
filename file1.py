# File Operations

"""
The files are two types :
     TEXT FILES : READABLE FORMAT 
     OBJECT FILES or BINARY FILES  : ENCRYPTED

     
"""

# open ==> read/write/append  ==> close


#open(<filepath>, <mode>)
"""
mode ==> r reading
mode ==> w writing
mode ==>> a appending

open function will returns a file obejct

"""

f = open('sample.txt', 'r')

data = f.read()  # returns entire data from the file as a string format
#print(type(data))
f.close()
print(data)
