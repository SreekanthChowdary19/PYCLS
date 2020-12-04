Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> x = [10, 20, 30, 40]
>>> 
>>> type(x)
<class 'list'>
>>> y = [50, 60, 70]
>>> type(y)
<class 'list'>
>>> x
[10, 20, 30, 40]
>>> y
[50, 60, 70]
>>> # Concatenation : Combining two list objects
>>> 
>>> # The operator (+) will act as a concatrnation operation
>>> 
>>> x+y
[10, 20, 30, 40, 50, 60, 70]
>>> z = x+y
>>> 
>>> z
[10, 20, 30, 40, 50, 60, 70]
>>> 
>>> type(z)
<class 'list'>
>>> len(z)
7
>>> x+ 10
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x+ 10
TypeError: can only concatenate list (not "int") to list
>>> 
>>> 
>>> 