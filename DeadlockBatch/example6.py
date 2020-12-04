Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1 = "BANGALORE"
>>> 
>>> s1
'BANGALORE'
>>> type(s1)
<class 'str'>
>>> s2 = 'HYDERABAD'
>>> type(s2)
<class 'str'>
>>> s2
'HYDERABAD'
>>> # SIZE OF STRING is TOTAL number of charcaers
>>> len(s1)
9
>>> len()s2
SyntaxError: invalid syntax
>>> 
>>> 
>>> len(s2)
9
>>> 
>>> # Operations:
>>> # concatenattion , Slicing , Indexing , Rept
>>> 
>>> s1
'BANGALORE'

>>> s1[0]
'B'
>>> s1[1]
'A'
>>> s1[2]
'N'
>>> s1[len(s1)-1]
'E'
>>> 
>>> s2
'HYDERABAD'

>>> s1+s2
'BANGALOREHYDERABAD'
>>> 
>>> s3 = s1 + " " + s2
>>> s3
'BANGALORE HYDERABAD'
>>> 
>>> 
>>> z = [10, 20, 30, 40, 50, 50, 60]
>>> z
[10, 20, 30, 40, 50, 50, 60]
>>> z[1:4]
[20, 30, 40]
>>> s3[0:4]
'BANG'
>>> 
>>> s1
'BANGALORE'
>>> s1*5
'BANGALOREBANGALOREBANGALOREBANGALOREBANGALORE'
>>> 
>>> #