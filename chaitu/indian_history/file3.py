# wap count each occurance of a word from the given file
f=open("New Text Document.txt","r")
data=f.read()
f.close()
words=data.split()
word_count={}
for word in words:
    if word not in word_count:
        word_count[word]=1
    else:
        word_count[word]=word_count[word]+1
print(word_count)
    
