# WAP count all the words from the about_india.txt file

# Get the data from the file
f = open('about_india.txt', "r")
data = f.read()
f.close()


#print(data)
words = data.split(" ")
print(len(words))
