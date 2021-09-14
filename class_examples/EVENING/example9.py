# WAP get the all the words which are starting with m and c
#from the given file

f =  open('about_india.txt', 'r')
data = f.read()
f.close()

words = data.split(" ")
#print(words)

for word in words:
    if word[0] == "m" or word[0] == "c":
        print(word)
