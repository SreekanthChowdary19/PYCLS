
# Write program find sum of all the sub sequnet
#elemets from the given list of list
x = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
import time
s = 0
for sub_list in x:
    #time.sleep(5)
    print(sub_list, type(sub_list))
    for ele in sub_list:
        #time.sleep(3)
        print(ele)
        s = s+ele
    print("========================")
print(s)

c = 0
for i in x[0]:
    c = c+i

for i in x[1]:
    c = c+i

    
    
