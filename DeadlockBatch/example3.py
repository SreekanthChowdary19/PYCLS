Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [10, 20, 30, 40, 50]
>>> 
>>> x
[10, 20, 30, 40, 50]
>>> 
>>> X[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    X[0]
NameError: name 'X' is not defined
>>> x[0]
10
>>> x[1]
20
>>> x[2]
30
>>> # To get last element
>>> 
>>> x[4]
50
>>> x
[10, 20, 30, 40, 50]
>>> 
>>> s = len(x)
>>> 
>>> s
5

>>> x[s-1]
50
>>> 
>>> x[len(x)-1]
50
>>> x
[10, 20, 30, 40, 50]
>>> 
>>> 
>>> x
[10, 20, 30, 40, 50]
>>> 
>>> x[0] = 100
>>> x
[100, 20, 30, 40, 50]

>>> 
>>> x[2] = 300
>>> 
>>> x
[100, 20, 300, 40, 50]

>>> x[len(x)-1] = 500
>>> x
[100, 20, 300, 40, 500]
>>> 
>>> 
>>> 