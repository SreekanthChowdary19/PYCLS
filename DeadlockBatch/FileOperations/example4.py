# Write a program count all the words from the given file
fobj = open("D:\\DeadlockBatch\\FileOperations\\India_History.txt","r")
data = fobj.read()
words=data.split()
print("The total number of words: ", len(words))
fobj.close()
