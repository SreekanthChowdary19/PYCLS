Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Define a list
>>> x = []
>>> x
[]
>>> len(x)
0
>>> type(x)
<class 'list'>
>>> 
>>> x = [10, 20, 30, 40]
>>> x
[10, 20, 30, 40]
>>> len(x)
4
>>> 
>>> x[0]
10
>>> x[1]
20
>>> x[len(x)]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x[len(x)]
IndexError: list index out of range
>>> 
>>> 
>>> x[4]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x[4]
IndexError: list index out of range
>>> 
>>> 
>>> 
>>> x
[10, 20, 30, 40]
>>> 
>>> 
>>> y = [50, 60, 70, 80]
>>> 
>>> y
[50, 60, 70, 80]
>>> type(y)
<class 'list'>
>>> 
>>> x
[10, 20, 30, 40]
>>> y
[50, 60, 70, 80]
>>> 
>>> x+y
[10, 20, 30, 40, 50, 60, 70, 80]
>>> 
>>> 
>>> 
>>> z = x+y
>>> z
[10, 20, 30, 40, 50, 60, 70, 80]

>>> len(z)
8
>>> 
>>> z[3:6]
[40, 50, 60]
>>> 
>>> z[1:]
[20, 30, 40, 50, 60, 70, 80]
>>> z[:6]
[10, 20, 30, 40, 50, 60]
>>> z = [10, 20, 30, 5, 50, 60]
>>> 
>>> z
[10, 20, 30, 5, 50, 60]
>>> 
>>> # change elements from list
>>> z
[10, 20, 30, 5, 50, 60]
>>> z[4] = 100000000
>>> 
>>> z
[10, 20, 30, 5, 100000000, 60]
>>> 
>>> 
>>> 
>>> x[4]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x[4]
IndexError: list index out of range
>>> 
>>> z[4]
100000000
>>> 
>>> 