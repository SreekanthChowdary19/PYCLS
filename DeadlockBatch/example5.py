Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [10, 20, 30, 40, 50]
>>> 
>>> x
[10, 20, 30, 40, 50]
>>> y = [60, 70, 80]
>>> 
>>> y
[60, 70, 80]
>>> z = x+y
>>> z
[10, 20, 30, 40, 50, 60, 70, 80]
>>> # Slicing operation
>>> z
[10, 20, 30, 40, 50, 60, 70, 80]
>>> 
>>> # SYNATX: list_var [lower_index: upper_index+1]
>>> 
>>> z[1:4]
[20, 30, 40]
>>> 
>>> z[3:7]
[40, 50, 60, 70]
>>> z[0:7]
[10, 20, 30, 40, 50, 60, 70]
>>> 
>>> # Passing a lower index and upper index is an optional
>>> 
>>> 
>>> # Default lower index is zero, upper index is SIZE+1
>>> 
>>> z
[10, 20, 30, 40, 50, 60, 70, 80]
>>> z[6:8]
[70, 80]
>>> 
>>> len(z)
8
>>> z[:5]
[10, 20, 30, 40, 50]
>>> z[5:]
[60, 70, 80]
>>> 
>>> z[:]
[10, 20, 30, 40, 50, 60, 70, 80]
>>> 
>>> 
>>> x
[10, 20, 30, 40, 50]
>>> 
>>> 
>>> y
[60, 70, 80]

>>> # Repetation operation
>>> 
>>> y*3
[60, 70, 80, 60, 70, 80, 60, 70, 80]
>>> 