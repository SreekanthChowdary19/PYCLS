Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> str1 = "BANGALORE"
>>> str1
'BANGALORE'
>>> type(str1)
<class 'str'>
>>> # Indexing : To fecth individual characters/elements
>>> 
>>> str1[0]
'B'
>>> str1[1]
'A'
>>> # To get the size or length : len()
>>> 
>>> len(str1)
9
>>> size = len(str1) - 1
>>> size
8
>>> str1[size]
'E'
>>> str2 = " CITY"
>>> str2
' CITY'
>>> type(str2)
<class 'str'>
>>> 
>>> 
>>> 
>>> 
>>> # Concatenation
>>> str1 + str2
'BANGALORE CITY'
>>> 
>>> str3 = str1 + str2
>>> 
>>> str3
'BANGALORE CITY'
>>> 
>>> # Slicing
>>> 
>>> str3[5:9]
'LORE'
>>> 
>>> str3[:11]
'BANGALORE C'
>>> str3[4:]
'ALORE CITY'
>>> str3[:]
'BANGALORE CITY'
>>> 
>>> 
>>> # Repetation
>>> str3 * 4
'BANGALORE CITYBANGALORE CITYBANGALORE CITYBANGALORE CITY'
>>> 
>>> # WAP convert given string from ANALYZE to ANALYSE
>>> 
>>> 
>>> str1 = "ANALYZE"
>>> str1
'ANALYZE'
>>> str1[4]
'Y'
>>> str1[5]
'Z'
>>> str1[5] = "S"
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    str1[5] = "S"
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> 
>>> str1[5] = 'S'
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    str1[5] = 'S'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> str1
'ANALYZE'
>>> 
>>> str1[0:5]
'ANALY'
>>> 
>>> str1[0:5]  + "S" + str1[len(str1)-1]
'ANALYSE'
>>> 
>>> 
>>> str1[0:5]  + "S" + str1[len(str1)-1]
'ANALYSE'
>>> 
>>> 
>>> str2 = "ANALYZE THE TOPIC"
>>> 
>>> 
>>> str2[:5] + "S" + str1[6:]
'ANALYSE'
>>> 
>>> 
>>> 
