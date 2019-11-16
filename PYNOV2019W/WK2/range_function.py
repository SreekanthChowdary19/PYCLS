Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # len(), type(), id()
>>> 
>>> # The range function raturns a range of elements
>>> 
>>> range(1, 10)
range(1, 10)
>>> listrange(1, 10)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    listrange(1, 10)
NameError: name 'listrange' is not defined
(
>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]
>>> # Signature : range([start=0], stop, [step=1])
>>> 
