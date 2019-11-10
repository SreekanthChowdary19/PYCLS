Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # List Demo
>>> 
>>> x = []
>>> 
>>> type(x)
<class 'list'>
>>> 
>>> # To get the size of any seq ==> len(seq)
>>> 
>>> len(x)
0
>>> x = [10, 20 ,30 ,40, 50]
>>> x
[10, 20, 30, 40, 50]
>>> type(x)
<class 'list'>
>>> len(x)
5
>>> # Access the 1st element
>>> x[0]
10
>>> x
[10, 20, 30, 40, 50]
>>> 
>>> x[1]
20
>>> x[2]
30
>>> x[4]
50
>>> size = len(x) -1
>>> size
4
>>> x[size]
50
>>> 
>>> x[len(x) - 1]
50
>>> x
[10, 20, 30, 40, 50]

>>> y = [60, 70, 80]
>>> y
[60, 70, 80]
>>> type(y)
<class 'list'>
>>> 
>>> x
[10, 20, 30, 40, 50]
>>> y
[60, 70, 80]

>>> x+y
[10, 20, 30, 40, 50, 60, 70, 80]
>>> 
>>> 
>>> 
>>> # Concatenation : Cobining two seq
>>> 
>>> x
[10, 20, 30, 40, 50]
>>> y
[60, 70, 80]
>>> # We can use  + operator for concatenation
>>> 
>>> x+y
[10, 20, 30, 40, 50, 60, 70, 80]
>>> z = x+y
>>> z
[10, 20, 30, 40, 50, 60, 70, 80]
>>> 
>>> type(z)
<class 'list'>
>>> len(z)
8
>>> # Slicing
>>> # SYNATX : list_var[l_index:u_index+1]
>>> 
>>> z[2:6]
[30, 40, 50, 60]
>>> 
>>> z[:4]  # by default lower index is zero
[10, 20, 30, 40]
>>> 
>>> z[4:]
[50, 60, 70, 80]
>>> 
>>> 
>>> # Repetaion
>>> 
>>> z
[10, 20, 30, 40, 50, 60, 70, 80]
>>> x
[10, 20, 30, 40, 50]
>>> 
>>> 
>>> x*3
[10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
>>> 
>>> x = [10, 12.5, "abc"]
>>> 
>>> type(x)
<class 'list'>
>>> 
>>> x = [[10, 20, 30], 10]
>>> 
>>> 
>>> # USing indexing we can change the elements
>>> 
>>> x = [10, 20, 30, 40]
>>> x
[10, 20, 30, 40]

>>> x[0] = 100
>>> x
[100, 20, 30, 40]
>>> 
>>> x[1] = 200
>>> x
[100, 200, 30, 40]

>>> x[len(x)-1] = 4000
>>> 
>>> x
[100, 200, 30, 4000]

>>> 
>>> 
