Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> x = {}
>>> 
>>> type(x)
<class 'dict'>
>>> 
>>> ist = {"KA": "BANGALORE", "TN": "CHENNAI", "KL": "Trivendrum"}
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'Trivendrum'}
>>> 
>>> ist["KA"]
'BANGALORE'
>>> ist["KL"]
'Trivendrum'
>>> # Dict is a mutable object
>>> # Adding a new key value pair to a existing dict
>>> #dict_var[KEY] = VALUE # SYNATX
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'Trivendrum'}
>>> ist["TS"] = "HYDERABAD"
>>> 
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'Trivendrum', 'TS': 'HYDERABAD'}
>>> 
>>> 
>>> 
>>> ist["AP"] = "HYDERABAD"
>>> 
>>> 
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'Trivendrum', 'TS': 'HYDERABAD', 'AP': 'HYDERABAD'}
>>> 
>>> 
>>> 
>>> # How to update existing key value
>>> 
>>> 
>>> # SYNTAX dict_var[KEY] = VALUE
>>> 
>>> ist['AP'] = "AMARAVATTHI"
>>> 
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'Trivendrum', 'TS': 'HYDERABAD', 'AP': 'AMARAVATTHI'}
>>> 
>>> 
>>> 
>>> ist["AP"] = ["KURNOOL", "AMARAVATHI", "VIZAG"]
>>> 
>>> ist
{'KA': 'BANGALORE', 'TN': 'CHENNAI', 'KL': 'Trivendrum', 'TS': 'HYDERABAD', 'AP': ['KURNOOL', 'AMARAVATHI', 'VIZAG']}
>>> 
>>> 
>>> 

>>> 
>>> ist["AP"]
['KURNOOL', 'AMARAVATHI', 'VIZAG']
>>> ist["AP"][1]
'AMARAVATHI'
>>> 