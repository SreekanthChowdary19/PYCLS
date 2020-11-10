# WAP find square of each and every element from the given list
#and display output in list format
import time

x = [2, 4, 6, 8]

y = [] # Place holder to store output
print("Input: ", x)
for ele in x:
    #time.sleep(10)
    y.append(ele*ele) # append()--> adds en element at the end of the list
    # y --> [4, 16, 36, 64]

    #print(y)
print("Output: ", y)
