f=open("D:\\update\\text.txt" ,"r")
data=f.read()
words=data.split()
word={}
for ele in words:
    if ele not in word:
        word[ele]=1
    else:
         word[ele]=word[ele]+1
print(word)
    

