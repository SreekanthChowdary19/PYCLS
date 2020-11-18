

f = open("D:\\DeadlockBatch\\FileOperations\\sample.txt", "r")


# to read the data from the file we have a function defined , read()
# the read() function reurns entire data from the file as a string


data = f.read()
print(data)


# close the file

f.close()
