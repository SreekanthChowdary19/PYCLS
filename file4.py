



def read_file(filepath):
    f = open(filepath, 'r')
    data = f.read() # returns entire data as a string fromat
    f.close()
    return data


