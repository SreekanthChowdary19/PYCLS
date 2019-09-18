x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
for row in x:
    #print(row)
    for e in row:
        print(e)
"""


for i in range(0, len(x)):
    for j in range(0, len(x)):
        if i == j:
            print(x[i][j])



