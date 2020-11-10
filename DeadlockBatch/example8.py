Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # Tuple
>>> # A tuple is used to store collection of elements
>>> # A tuple is also a sequenial data type
>>> 
>>> # To represent a tuple we can use --> ()
>>> 
>>> x = []
>>> type(x)
<class 'list'>
>>> x = ()
>>> 
>>> type(x)
<class 'tuple'>
>>> 
>>> x = (10, 20, 30, 40, 50)
>>> x
(10, 20, 30, 40, 50)
>>> 
>>> # Indexing : To access individual elements
>>> 
>>> x[0]
10
>>> x[1]
20
>>> # size
>>> len(x)
5
>>> # last elements
>>> x[len(x)-1]
50
>>> 
>>> x
(10, 20, 30, 40, 50)
>>> # Concatenation (=)
>>> # Concatenation (+)
>>> x
(10, 20, 30, 40, 50)
>>> 
>>> y = (60, 70, 80)
>>> y
(60, 70, 80)
>>> type(y)
<class 'tuple'>
>>> z = x+y
>>> z
(10, 20, 30, 40, 50, 60, 70, 80)
>>> 
>>> len(z)
8
>>> # Extracting sub seq from the given seq Z
>>> 
>>> z[2:6]
(30, 40, 50, 60)
>>> z[2:]
(30, 40, 50, 60, 70, 80)
>>> z[:6]
(10, 20, 30, 40, 50, 60)
>>> y*5
(60, 70, 80, 60, 70, 80, 60, 70, 80, 60, 70, 80, 60, 70, 80)
>>> y
(60, 70, 80)
>>> 
>>> 
>>> y[0] = 100
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    y[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> adhars = [1, 2, 3]
>>> 
>>> 