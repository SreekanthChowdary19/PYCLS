Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> # split() vs join()  --> string functions
>>> 
>>> 
>>> 
>>> s= "Welcome to python world and Welcome to new era of life"
>>> 
>>> s
'Welcome to python world and Welcome to new era of life'
>>> 
>>> s.split(' ')
['Welcome', 'to', 'python', 'world', 'and', 'Welcome', 'to', 'new', 'era', 'of', 'life']
>>> s.split()
['Welcome', 'to', 'python', 'world', 'and', 'Welcome', 'to', 'new', 'era', 'of', 'life']
>>> s.split('to')
['Welcome ', ' python world and Welcome ', ' new era of life']
>>> 
>>> 
>>> x = ["ABCD", "XYZ", "MNO"]
>>> 
>>> x
['ABCD', 'XYZ', 'MNO']
>>> 
>>> s = "======="
>>> 
>>> s
'======='
>>> s.join(x)
'ABCD=======XYZ=======MNO'
>>> 
>>> ip = "10.98.78.10"
>>> 
>>> 
>>> ip
'10.98.78.10'
>>> d = ip.split(".")
>>> 
>>> d
['10', '98', '78', '10']
>>> 
>>> 
>>> ".".join(d)
'10.98.78.10'
>>> 
>>> "-".join(d)
'10-98-78-10'
>>> x
['ABCD', 'XYZ', 'MNO']
>>> 
>>> 
>>> "-".join(x)
'ABCD-XYZ-MNO'
>>> 
>>> 
>>> 