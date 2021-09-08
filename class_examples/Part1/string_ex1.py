Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1 = "BANGALORE"
>>> s
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s1
'BANGALORE'
>>> s1[0]
'B'
>>> s1[1]
'A'
>>> s2 = "CITY"
>>> s1+s2
'BANGALORECITY'
>>> s1(0)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s1(0)
TypeError: 'str' object is not callable
>>> 
>>> 
>>> 
>>> s3 = s1 + " " + s2
>>> 
>>> 
>>> 
>>> s3
'BANGALORE CITY'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s3[5:8]
'LOR'
>>> 
>>> 
>>> s3[4:]
'ALORE CITY'
>>> 
>>> s3[:8]
'BANGALOR'
>>> 
>>> 
>>> 
>>> 
>>> s3[:]
'BANGALORE CITY'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> len(s3)
14
>>> 
>>> 
>>> s3
'BANGALORE CITY'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s1 = "BANGALORE"
>>> 
>>> 
>>> s1
'BANGALORE'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s1[0] = "M"
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s1[0] = "M"
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> 
>>> s1
'BANGALORE'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s1["B"] = "M"
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s1["B"] = "M"
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> s1 = "MANGALORE"
>>> 
>>> s1
'MANGALORE'
>>> 
>>> 
>>> 
>>> s1
'MANGALORE'
>>> 
>>> 
>>> s1 = "BAMGALORE"
>>> 
>>> 
>>> s1 = "BANGALORE"
>>> 
>>> 
>>> 
>>> s1
'BANGALORE'
>>> 
>>> 
>>> 
>>> s1[1:]
'ANGALORE'
>>> 
>>> 
>>> 
>>> 
>>> "M" + s1[1:]
'MANGALORE'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 