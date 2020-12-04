import os

path = "/home/bobby"
resp = os.walk(path)

#print(type(resp))
c = 0
for root, folders, files in resp:
    for f in files:
        if f.endswith('.py'):
            #print(f)coordinate.py
            if f == "coordinate.py":
                #path = root + "/" + f
                path = os.path.join(root, f)
                print(path)
                obj = open(path, "r")
                data = obj.read()
                obj.close()
                print(data)
    
