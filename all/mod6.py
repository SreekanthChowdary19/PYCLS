# File Operations

f = open('input.txt', 'r')

# read() or readlines()

resp = f.readlines()

f.close()
for data in resp:
    print(type(data))