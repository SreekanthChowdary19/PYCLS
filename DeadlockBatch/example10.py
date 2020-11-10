Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [10, 20, 30, 40]
>>> x
[10, 20, 30, 40]
>>> # append(element) --> Adds element at the end of the list
>>> 
>>> x.append(5)
>>> x
[10, 20, 30, 40, 5]
>>> x.append(50)
>>> x
[10, 20, 30, 40, 5, 50]
>>> # insert(index_position, element)
>>> x.insert(2, 15)
>>> x
[10, 20, 15, 30, 40, 5, 50]
>>> 
>>> 
>>> 
>>> x.insert(0, 15)
>>> x
[15, 10, 20, 15, 30, 40, 5, 50]
>>> 
>>> 
>>> x.append(20)
>>> x.append(10)
>>> x
[15, 10, 20, 15, 30, 40, 5, 50, 20, 10]

>>> 
>>> # pop(<position>) # by default deletes last element
>>> 
>>> x.pop(4)
30
>>> x.pop()
10
>>> x
[15, 10, 20, 15, 40, 5, 50, 20]
>>> # remove(element)
>>> 
>>> x.remove(40)
>>> x
[15, 10, 20, 15, 5, 50, 20]
>>> x.remove(20) # deletes 1st occurance of 20
>>> 
>>> x
[15, 10, 15, 5, 50, 20]

>>> x
[15, 10, 15, 5, 50, 20]
>>> x.sort()
>>> 
>>> x
[5, 10, 15, 15, 20, 50]
>>> 
>>> 
>>> x.reverse()
>>> 
>>> x
[50, 20, 15, 15, 10, 5]

>>> # dir