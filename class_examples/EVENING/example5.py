# open --> read/write/append --> close
"""
When we are opening a file in write mode
if the file does not exist it will create a new file or if the file
is alredy exist the data will be overridden
"""
# opening a file 
f = open("C:\\Users\\91998\\Desktop\\class_examples\EVENING\\output.txt", "a")
f.write("\nI am expecting package 8 lac")
f.close()
