Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Strings
>>> 
>>> # We can define  either single quotes or double quotes
>>> 
>>> 
>>> str1 = 'Banaglore'
>>> type(str1)
<class 'str'>
>>> 
>>> str2 = "Hyderabad"
>>> str2
'Hyderabad'
>>> type(str2)
<class 'str'>
>>> 
>>> # A string sequential object, SO the operation we have perfromed for
>>> # list obejct like indexing , concatenation , slicing , rept, size are
>>> # even applicable for string object
>>> 
>>> # Indexing
>>> str1[0]
'B'
>>> str1[1]
'a'
>>> len(str1)
9
>>> 
>>> 
>>> 
>>> str1[len(str1)-1]
'e'
>>> 
>>> # Concatenation
>>> 
>>> str1
'Banaglore'
>>> str2 = " City"
>>> 
>>> str2
' City'
>>> str1 + str2
'Banaglore City'
>>> str3 = str1 + str2
>>> str3
'Banaglore City'
>>> # Slicing : To extract sub seq from the given seq
>>> 
>>> str1[0:5]
'Banag'
>>> 
>>> str1[:4]
'Bana'
>>> str1[6:]
'ore'
>>> str1 * 3
'BanagloreBanagloreBanaglore'
>>> 
>>> # WAP convert given string from BANGALORE to MANGALORE
>>> 
>>> str1 = "BANGALORE"
>>> 
>>> str1
'BANGALORE'
>>> str1[0] = 'M'
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    str1[0] = 'M'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> # Strngs are constant objects or read-only objects in python
>>> "M" + str1[1:]
'MANGALORE'
>>> 
>>> 
