
def write_file(filepath, content, mode='w'):
    f = open(filepath, mode)
    f.write(content) # content should be string
    f.close()




