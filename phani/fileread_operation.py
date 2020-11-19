f=open("C:\\Users\\garya\\OneDrive\\Desktop\\checkin Git\\gphani.txt","r")
Data=f.read()
f.close()
words=Data.split()
wordcount={}
for word in words:
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word]=wordcount[word]+1
print(wordcount)


    
