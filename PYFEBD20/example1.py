Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> # Built-in functions for list objcet
>>> 
>>> x = [10, 20, 30, 40]
>>> x
[10, 20, 30, 40]
>>> type(x)
<class 'list'>
>>> 
>>> # Add the element at the end
>>> x
[10, 20, 30, 40]
>>> # append(element) ==> Adds the element at the end of the list
>>> # insert(index, element) ==> Adds the element at the given index position
>>> 
>>> x
[10, 20, 30, 40]
>>> x.append(60)
>>> x
[10, 20, 30, 40, 60]
>>> x.append(5)
>>> x
[10, 20, 30, 40, 60, 5]
>>> x.append(20)
>>> x
[10, 20, 30, 40, 60, 5, 20]
>>> x.insert(2, 15)
>>> x
[10, 20, 15, 30, 40, 60, 5, 20]
>>> x.insert(0, 100)
>>> x
[100, 10, 20, 15, 30, 40, 60, 5, 20]
>>> x.insert(1, 20)
>>> 
>>> x
[100, 20, 10, 20, 15, 30, 40, 60, 5, 20]
>>> 
>>> x
[100, 20, 10, 20, 15, 30, 40, 60, 5, 20]
>>> 
>>> 
>>> # To delelte the elements from the list
>>> # remove(element)
>>> # pop(index), pop() ==> default last index
>>> 
>>> x
[100, 20, 10, 20, 15, 30, 40, 60, 5, 20]
>>> 
>>> x.pop()
20
>>> 
>>> x
[100, 20, 10, 20, 15, 30, 40, 60, 5]
>>> x.pop(4)
15
>>> 
>>> x
[100, 20, 10, 20, 30, 40, 60, 5]
>>> 
>>> x.remove(60)
>>> x
[100, 20, 10, 20, 30, 40, 5]
>>> 
>>> x.remove(20) # deletes the 1st occurance of 20
>>> x
[100, 10, 20, 30, 40, 5]
>>> 
>>> # Arrange the list
>>> 
>>> x
[100, 10, 20, 30, 40, 5]

>>> 
>>> x.sort()
>>> 
>>> x
[5, 10, 20, 30, 40, 100]

>>> 
>>> x.reverse()
>>> x
[100, 40, 30, 20, 10, 5]

>>> 
================================ RESTART: Shell ================================
>>> 
>>> 
>>> x = "XYZ"
>>> x.reverse()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    x.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> 
>>> 
>>> # To list the functions defined for the specific object
>>> 
>>> # dir()
>>> 
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> # __method__ dunder methods or dunder attributes
>>> 
>>> help(x.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> x = []
>>> 
>>> help(x.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> 
>>> 
>>> 
>>> x = [10, 20, 30, 30, 40, 30, 90]
>>> 
>>> x
[10, 20, 30, 30, 40, 30, 90]

>>> x.count(3)
0
>>> 
>>> 
>>> x.count(30)
3
>>> 
>>> 
>>> x.count(40)
1
>>> 
>>> x
[10, 20, 30, 30, 40, 30, 90]
>>> 
>>> 
>>> x.index(2)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    x.index(2)
ValueError: 2 is not in list
>>> x.index(20)
1
>>> 
>>> x.index(30)
2
>>> 
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> dir(())
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x = 10, 20, 30
>>> 
>>> 
>>> x
(10, 20, 30)

>>> 
>>> 
