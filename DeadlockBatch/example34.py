Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> d = {}

>>> type(d)
<class 'dict'>
>>> 
>>> d = {"A": 65, "B": 66, "C": 67, "D": 68}
>>> 
>>> #  A, B, C, D are the keys
>>> 
>>> # 65, 66, 67, 68 are the values inside a dict
>>> 
>>> # is there relation between key & value
>>> # To access value you shoud know key
>>> d["A"]
65
>>> d["B"]
66
>>> d.keys()
dict_keys(['A', 'B', 'C', 'D'])
>>> d.values()
dict_values([65, 66, 67, 68])
>>> d.items()
dict_items([('A', 65), ('B', 66), ('C', 67), ('D', 68)])
>>> 
>>> 
>>> 