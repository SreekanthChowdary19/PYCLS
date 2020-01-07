import csv


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

