# WAP count each occurance of a word from the given file



def read_file(filepath):
    f = open(filepath, 'r')
    data = f.read() # returns entire data as a string fromat
    f.close()
    return data

def count_words(text):
    words = text.split()
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] = d[word] + 1
    return d

def main():
    resp = read_file('sample.txt')
    count = count_words(resp)
    return count

print(main())


