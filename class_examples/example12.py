Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> # A list is  a Mutable object
>>> 
>>> x = [10, 20, 30, 40]
>>> 
>>> x
[10, 20, 30, 40]
>>> 
>>> # The mutable objects allows in-place change
>>> # And also a list may can grow or shrink
>>> # Re-arranging the elements from the list
>>> x
[10, 20, 30, 40]
>>> # Adding ==> append(<element>)  insert(<index>, elements)
>>> 
>>> # Delete ==>  pop(<index>), remove(<element>)
>>> 
>>> # Order ==> sort()  , reverse()
>>> 
>>> x
[10, 20, 30, 40]
>>> x.append(25) # adds the element at the end of the list
>>> x
[10, 20, 30, 40, 25]
>>> x.append(50) # adds the element at the end of the list
>>> 
>>> x
[10, 20, 30, 40, 25, 50]
>>> 
>>> 
>>> x.append(20) # adds the element at the end of the list
>>> 
>>> x
[10, 20, 30, 40, 25, 50, 20]

>>> 
>>> x.insert(3, 35)
>>> 
>>> x
[10, 20, 30, 35, 40, 25, 50, 20]

>>> 
>>> x.insert(0, 70)
>>> 
>>> x
[70, 10, 20, 30, 35, 40, 25, 50, 20]
>>> 
>>> 
>>> x
[70, 10, 20, 30, 35, 40, 25, 50, 20]
>>> 
>>> 
>>> x.pop(2) # Removes the element at the index position 2
20
>>> x
[70, 10, 30, 35, 40, 25, 50, 20]
>>> 
>>> 
>>> x.pop()  # Removes by default last eleement
20
>>> 
>>> x
[70, 10, 30, 35, 40, 25, 50]

>>> 
>>> 
>>> x.remove(30) # Removes the element 30
>>> 
>>> x
[70, 10, 35, 40, 25, 50]
>>> 
>>> 
>>> x.append(10)
>>> 
>>> x.append(10)
>>> x
[70, 10, 35, 40, 25, 50, 10, 10]
>>> 
>>> 
>>> x.remove(10) # Removes 1st occurance element
>>> 
>>> x
[70, 35, 40, 25, 50, 10, 10]

>>> 
>>> 
>>> x
[70, 35, 40, 25, 50, 10, 10]
>>> 
>>> 
>>> # sort()
>>> x.sort()
>>> x
[10, 10, 25, 35, 40, 50, 70]

>>> 
>>> #reverse()
>>> x.reverse()
>>> x
[70, 50, 40, 35, 25, 10, 10]
>>> 
>>> # Python is very easy langauge
>>> # dir() it will list down the methods or attributes defined for specific object
>>> 
>>> 
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x
[70, 50, 40, 35, 25, 10, 10]
>>> 
>>> 
>>> help(x.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> 
>>> 
>>> x.count(10)
2
>>> 
>>> x
[70, 50, 40, 35, 25, 10, 10]

>>> 
>>> x.index(40)
2
>>> 
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
