import csv


import psutil
data = []

for proc in psutil.process_iter():
    x = proc.name(), proc.pid
    data.append(list(x))
#print(y)




header = ["ProceesName", "PID"]
f =  open('process2.csv', 'w')

workbook = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

workbook.writerow(header)
for datils in data:
    print(datils)
    workbook.writerow(datils)

f.close()

"""


data = [['p1', '100', '1000'],
['p2', '101', '1001'], ['p3', '102', '1003']]

header = ["ProceesName", "Memory", "PID"]
f =  open('process.csv', 'w')

workbook = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

workbook.writerow(header)
for datils in data:
    print(datils)
    workbook.writerow(datils)

f.close()
"""
