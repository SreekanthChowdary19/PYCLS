d = {"A" : [10, 20, 30, 40], "B": [50, 60, 70]}

for k in d:
    print(d[k])
    for i in d[k]:
        print(i)

#keyS() values() items()


for values in d.values():
    print(values)
