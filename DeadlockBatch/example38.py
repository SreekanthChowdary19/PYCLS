# WAP print all the numbers from the list contains from 1 to 100 except the
# elements which are divisble by 4


x = range(1, 101)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16........22, 23, 24......96, 97,...100]
"""
for ele in x:
    if ele % 4 !=0 :
        print(ele)
    else:
        print("Element is skippedd : ", ele)
"""

for ele in x:
    if ele % 4 == 0:
        continue
    print(ele)
        
