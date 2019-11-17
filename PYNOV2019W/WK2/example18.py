# Write a program print all the words which are strating with letter 's'
f = open('sample.txt', 'r')

data = f.read() # retunrs content from the file as astring
f.close()

words = data.split()  # words are type list of strings ["sam", "ram", "san", "dan"]

#print(len(words))
#words = ["sam", "ram", "san", "dan"]
for word in words:
     if word[0] == 's':
          print(word)
     
