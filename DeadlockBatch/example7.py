Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # WAP convert given string from BANGALORE to MANGALORE
>>> 
>>> s = "BANGALORE"
>>> 
>>> s[0] = "M"
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s[0] = "M"
TypeError: 'str' object does not support item assignment
>>> s[1:]
'ANGALORE'
>>> "M" + s[1:]
'MANGALORE'
>>> 
>>> 