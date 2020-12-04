# WAP count each occurance of a word from the given file


f = open('India_History.txt', 'r')
data = f.read() # type of data is a string 
f.close()


words = data.split()  # split the string with space , returns a list of strings type


# traverse list to get the each word (element) from the list of strings

word_count = {} # place holder to store the output
for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] = word_count[word] +1
print(word_count)
        


