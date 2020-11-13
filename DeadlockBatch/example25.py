# Replace each sub list with some of respctive elements 
#x = [[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 200, 300]]

x = [[10, 20, 30, 40], [40, 50, 60], [70, 80, 90, 100], [100, 200, 300, 400]]

"""
for i in range(0, len(x)):
    S = sum(x[i])
    x[i] = S
print(x)
"""


for i in range(0, len(x)):
    s = 0
    for e in x[i]:
        s = s+e
    x[i] = s
print(x)
    
