# WAP count all the words from the file sample,txt


f = open('sample.txt', 'r')

data = f.read() # retunrs content from the file as astring
f.close()

words = data.split()  # words are type list of strings ["sam", "ram", "san", "dan"]

#print(len(words))
