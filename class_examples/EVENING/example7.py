Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # spilt vs join
>>> s1 = "India was in past, India is in present, and India will be in future."
>>> s1
'India was in past, India is in present, and India will be in future.'
>>> s1.split(",")
['India was in past', ' India is in present', ' and India will be in future.']
>>> x = s1.split(",")
>>> x
['India was in past', ' India is in present', ' and India will be in future.']
>>> x = s1.split("in")
>>> x
['India was ', ' past, India is ', ' present, and India will be ', ' future.']
>>> ip = "10.221.50.98"
>>> ip.split(".")
['10', '221', '50', '98']
>>> 
>>> 
>>> 
>>> 
>>> ip.split(".")
['10', '221', '50', '98']
>>> 
>>> 
>>> 
>>> a = ["A", "B", "C", "D"]
>>> a
['A', 'B', 'C', 'D']
>>> 
>>> 
>>> str1 = "-PYTHON-"
>>> str1.join(a)
'A-PYTHON-B-PYTHON-C-PYTHON-D'
>>> 
>>> 
>>> 
>>> x = ip.split(".")
>>> 
>>> x
['10', '221', '50', '98']
>>> 
>>> ".".join(x)
'10.221.50.98'
>>> 
>>> 
>>> 