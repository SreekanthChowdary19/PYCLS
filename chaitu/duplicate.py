#wap print all duplicate values in descending order from the given input list
a=[401,403,409,403,453,402,438,401,444]
a.sort()
b=a[1:4]
b.reverse()
b.remove(402)
print(b)

"""
c=[401, 401, 402, 403, 403, 409, 438, 444, 453]
>>> c.[1:4]
SyntaxError: invalid syntax
>>> c[1:4]
[401, 402, 403]
>>> a=c[1:4]
>>> a
[401, 402, 403]
>>> a.remove(402)
>>> a
[401, 403]
>>> a.reverse()
>>> a
[403, 401]
>>> """
