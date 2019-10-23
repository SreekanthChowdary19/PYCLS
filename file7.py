"""
If we are opening a file in write mode the file not exist , it will create a new fle

If the file alrady exist it will overide the data
"""
"""
f = open('output.txt', 'w')

f.write("Hello Welcome to Python")

f.close()

"""

f = open('output.txt', 'w')
f.write("Python is very easy programming")
f.close()


f = open('output.txt', 'a')

f.write("Hello Welcome to Python")

f.close()
