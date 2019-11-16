Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # List Functions
>>> 
>>> x = [10, 9, 45, 69, 87, 45, 79]
>>> x
[10, 9, 45, 69, 87, 45, 79]
>>> 
>>> len(x)
7
>>> # Add element at the end ==> append(element)
>>> 
>>> x.append(100)
>>> x
[10, 9, 45, 69, 87, 45, 79, 100]
>>> x.append(10)
>>> x.append(10)
>>> x
[10, 9, 45, 69, 87, 45, 79, 100, 10, 10]
>>> # Add the element based on position given ==> insert(index, element)
>>> x.insert(4, 60)
>>> x
[10, 9, 45, 69, 60, 87, 45, 79, 100, 10, 10]
>>> x.insert(0, 64)
>>> x
[64, 10, 9, 45, 69, 60, 87, 45, 79, 100, 10, 10]
>>> 
>>> 
>>> # To delete element based on postion given==> pop([index])
>>> # by default it deletes last element
>>> x
[64, 10, 9, 45, 69, 60, 87, 45, 79, 100, 10, 10]
>>> 
>>> x.pop()
10
>>> x
[64, 10, 9, 45, 69, 60, 87, 45, 79, 100, 10]
>>> 
>>> # To delete element directly ==> remove(element)
>>> x.remove(87)
>>> x
[64, 10, 9, 45, 69, 60, 45, 79, 100, 10]
>>> 
>>> x.pop(2)
9
>>> x
[64, 10, 45, 69, 60, 45, 79, 100, 10]
>>> x
[64, 10, 45, 69, 60, 45, 79, 100, 10]
>>> 
>>> 
>>> x.remove(10) # deletes 1st occurances of value 10
>>> 
>>> x
[64, 45, 69, 60, 45, 79, 100, 10]
>>> 
>>> 
>>> 
>>> 
>>> x
[64, 45, 69, 60, 45, 79, 100, 10]
>>> 
>>> x.sort()
>>> x
[10, 45, 45, 60, 64, 69, 79, 100]
>>> 
>>> x.reverse()
>>> x
[100, 79, 69, 64, 60, 45, 45, 10]
>>> 
>>> 
>>> # dir() function list down all the function available for a particular object
>>> 
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> help(x.count) # list.count
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> 
>>> 
>>> x
[100, 79, 69, 64, 60, 45, 45, 10]
>>> 
>>> x.count(69)
1
>>> x.count(45)
2
>>> str.append()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    str.append()
AttributeError: type object 'str' has no attribute 'append'
>>> "apcd"
'apcd'
>>> c = "abcd"
>>> c
'abcd'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
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
>>> 
>>> 
>>> 
>>> x
[100, 79, 69, 64, 60, 45, 45, 10]
>>> 
>>> x.index(69)
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
>>> 
>>> 
