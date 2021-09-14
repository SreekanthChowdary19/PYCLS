# WAP count how many times the word India is repeated 

# Get the data from the file
f = open('about_india.txt', "r")
data = f.read()
f.close()


#print(data)
words = data.split(" ")
#print(words)

c = 0
for word in words:
    if word == "India":
        #print(word)
        c = c+1
print(c)
