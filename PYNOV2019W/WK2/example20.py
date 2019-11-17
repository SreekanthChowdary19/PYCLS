# Reading the data from the file file1.txt and file2.txt

# Print all the words which are starts with s or m from the file1

# print all the words which are strats with c or h from the file 2



# read the data from file1

f = open('file1.txt', 'r')
data1 = f.read()
f.close()

words_f1 = data1.split()
list_f1 = []
for word_f1 in words_f1:
     if word_f1[0] == 's' or word_f1[0] == 'm':
          list_f1.append(word_f1)

print(list_f1)
print("="*50)

f = open('file2.txt', 'r')
data2 = f.read()
f.close()

words_f2 = data2.split()

list_f2 = []

for word_f2 in words_f2:
     if word_f2[0] == 'c' or word_f2 == 'h':
          list_f2.append(word_f2)
print(list_f2)
