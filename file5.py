# WAP count each occurance of a word from the given file



def read_file(filepath):
    f = open(filepath, 'r')
    data = f.read() # returns entire data as a string fromat
    f.close()
    return data


resp = read_file('sample.txt')
words = resp.split()

d = {}
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] = d[word] + 1
print(d)
    
