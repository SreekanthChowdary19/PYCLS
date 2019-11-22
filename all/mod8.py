# Retriving object information form the file we can it is object
# de-serilization also called it as unpickling

import pickle

f = open('input.pkl', 'rb')

data1 = pickle.load(f)

data2 = pickle.load(f)

print(data1, type(data1))

print(data2, type(data2))

f.close()