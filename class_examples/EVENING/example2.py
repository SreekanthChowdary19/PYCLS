# FILE OPERATIONS
"""
open --> write --> close

open --> read  --> close

open --> append --> close
"""
#open --> write/read/append --> close


#fileobject open(filepath, mode)
"""
filepath: STRING
mode : STRING

mode --> r, w, a
fileobject : It handler to the file operations
"""

# read() - returns entire data as a STRING
# close()

f = open("C:\\Users\\91998\\Desktop\\class_examples\EVENING\\about_india.txt", "r")
data = f.read()
f.close()
print(type(data))
print(data)








