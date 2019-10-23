# Write a program count the number of words from the given file sample.txt


f = open('sample.txt', 'r')
data = f.read()
f.close()


# data

words = data.split()

print("Number of words in sample.txt")
print(len(words))



# Write a program count the total number of words from the test.txt

f = open('test.txt', 'r')
data = f.read()
f.close()

words_in_file2 = data.split()
print("Number of words in test.txt")
print(len(words_in_file2))
