Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # Dictionaries
>>> 
>>> # Non-sequential object
>>> 
>>> # Dict is collection of elements
>>> # Element contains two thing i.e key and value
>>> # To define == > {}
>>> 
>>> d = {}
>>> 
>>> type(d)
<class 'dict'>
>>> d = {"A": 65, "B": 66, "C": 67, "D": 68}
>>> d
{'A': 65, 'B': 66, 'C': 67, 'D': 68}
>>> # To access dict values we have to use keys
>>> # SYNTAX
>>> d["A"]
65
>>> d["B"]
66
>>> d["D"]
68
>>> d["X"]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d["X"]
KeyError: 'X'
>>> d.keys()
dict_keys(['A', 'B', 'C', 'D'])
>>> d.values()
dict_values([65, 66, 67, 68])
>>> d.values()
dict_values([65, 66, 67, 68])
>>> 
>>> 
>>> d.items()
dict_items([('A', 65), ('B', 66), ('C', 67), ('D', 68)])
>>> 
>>> # Dicts are mutable objects
>>> 
>>> ist = {"KA": "BANGALORE", "TN": "CHENNAI", "KL": "TRIVENDRUM"}
>>> 
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'TRIVENDRUM'}
>>> 
>>> 
>>> ist["KA"]
'BANGALORE'
>>> ist["TN"]
'CHENNAI'
>>> 
>>> # How to add a new key value pair to existing dictinary
>>> 
>>> # SYNATX
>>> 
>>> #dict_name[KEY] = VALUE
>>> 
>>> ist["TS"] = "HYDERABAD"
>>> 
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'TRIVENDRUM', 'TS': 'HYDERABAD'}
>>> 
>>> 
>>> 
>>> ist["AP"] = "HYDERABAD"
>>> 
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'TRIVENDRUM', 'TS': 'HYDERABAD', 'AP': 'HYDERABAD'}
\
>>> 
>>> 
>>> # Note: Dict values may be duplicate but keys must be unique
>>> 
>>> # How to update existing dict values
>>> 
>>> #dict_name[KEY] = Value
>>> 
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'TRIVENDRUM', 'TS': 'HYDERABAD', 'AP': 'HYDERABAD'}
>>> 
>>> ist["AP"] = "AMARAVATHI"
>>> 
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'TRIVENDRUM', 'TS': 'HYDERABAD', 'AP': 'AMARAVATHI'}
>>> 
>>> 
