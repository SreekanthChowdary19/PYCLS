# Write a program count each word from the given file sample.txt





# Reading the data from the file

f = open('sample.txt', 'r')
data = f.read()
f.close()

words = data.split()


# Counting the words
d  = {}

for word in words:
     if word not in d:
          d[word] = 1
     else:
          d[word] = d[word] + 1
print(d)
