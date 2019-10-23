def read_file(filepath):
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data


def count_words(str_input):
    words = str_input.split()
    return len(words)


output = read_file('sample.txt')
print(count_words(output))
#words  = output.split()
#count = len(words)
#print(count)


output = read_file('test.txt')
print(count_words(output))
#words  = output.split()
#count = len(words)
#print(count)
