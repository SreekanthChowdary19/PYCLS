
# Storing python objects as object (bytes) in a file
# We can call it as a object serilization (pickling)
# We can achive with binary files

import pickle


x  = [10, 20, 30, 40]  # Python Object

d = {"A": 65, "B": 66, "D": 68} # Object

f = open('input.pkl', 'wb')

pickle.dump(x, f)
pickle.dump(d, f)

f.close()

