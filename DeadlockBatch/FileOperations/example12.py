# WAP read the data from file1 and file2 and display all the words from the file1 which are starts with
#'s' and 'm' and from the file2 get all the words which are starts wig c , h



def file_read(filepath):
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    print(data)

file_read('file1.txt')

print("="*100)
file_read("file2.txt")

"""
f2 = open('file2.txt', 'r')
data2 = f2.read()
f2.close()

words1 = data1.split()
output1 = []

for word in words1:
    if word[0] == 's' or word[0] =='m':
        output1.append(word)
print(output1)

words2 = data2.split()
output2 = []
for word in words2:
    if word[0] == 'c' or word[0] == 'h':
        output2.append(word)
print(output2)
"""
