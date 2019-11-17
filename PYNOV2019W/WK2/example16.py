"""
Files are two types

Text Files  - Human readble format

Binary Files - Object files
"""

"""

open write close

open read close

open update close


open ==> read/write/append ==> close
"""


# To open a file we can use open() function

"""
open(<filepath>, <mode>)

mode param will tell, what purpose we are opening a file

r ==> reading
w ==> Writing
a ==> appending


it return the file obejct ==> To perfrom further read/write/append
we have to use the file object
"""
# To read the data from the file ==> read()
"""
The read function returns entire data from the file as a string
"""
# To close the file we can use ==> close()


f = open('sample.txt', 'r')

data = f.read()

f.close()


print(data)














