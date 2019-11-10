Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = []
>>> 
>>> type(x)
<class 'list'>
>>> 
>>> x = ()
>>> 
>>> type(x)
<class 'tuple'>
>>> 
>>> x = (10, 20, 30, 40, 50)
>>> x
(10, 20, 30, 40, 50)

>>> x[0]
10
>>> x[a]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x[a]
NameError: name 'a' is not defined
>>> x[1]
20
>>> x[len(x)-1]
50
>>> x
(10, 20, 30, 40, 50)
>>> 
>>> y = (60, 70, 90)
>>> y
(60, 70, 90)
>>> type(y)
<class 'tuple'>
>>> x+y
(10, 20, 30, 40, 50, 60, 70, 90)
>>> z = x+y
>>> z
(10, 20, 30, 40, 50, 60, 70, 90)
>>> 
>>> z[2:7]
(30, 40, 50, 60, 70)
>>> x*5
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
>>> x = (10, 12.5)
>>> x
(10, 12.5)
>>> 
>>> x = (10, 20, 30)
>>> x
(10, 20, 30)
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> # Tuple also read-only or constant object like strings
>>> 
