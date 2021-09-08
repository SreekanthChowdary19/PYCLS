Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [10, 20, 30]
>>> x
[10, 20, 30]
>>> x[0] = 10000
>>> x
[10000, 20, 30]
>>> y = [10, 20, 30]
>>> y
[10, 20, 30]
>>> y = (10, 20, 30)
>>> y[0] = 10000
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    y[0] = 10000
TypeError: 'tuple' object does not support item assignment
>>> 