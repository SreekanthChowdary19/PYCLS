# Write a program count the words which are starting with letter p
fobc=open("D:\\DeadlockBatch\\FileOperations\\India_History.txt","r")
data=fobc.read()
words=data.split()
output = []
for word in words:
    if word[0]=="p":
        output.append(word)

print("Words: " , output)
print("Lengtht of word", len(output))    
    
    
