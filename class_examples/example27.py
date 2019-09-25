Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> ist = {"KA": "BANAGLORE", "KL": "TRIVENDRUM", "TN": "CHENNAI}
       
SyntaxError: EOL while scanning string literal
>>> 
>>> ist = {"KA": "BANAGLORE", "KL": "TRIVENDRUM", "TN": "CHENNAI"}
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNAI'}
>>> 
>>> # Dicts are mutable object
>>> # Dict keys immutable object
>>> # Dict values any python object
>>> ist = {"KA": "BANAGLORE", "KL": "TRIVENDRUM", "TN": "CHENNAI"}
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNAI'}
>>> # How to add new key value pair to a existing dict
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNAI'}
>>> # SYNTAX
>>> dict_name["KEY"] = <VALUE>
SyntaxError: invalid syntax
>>> ist["TS"] = "HYDERABAD"
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNAI', 'TS': 'HYDERABAD'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ist["AP"] = "HYDERABAD"
>>> 
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNAI', 'TS': 'HYDERABAD', 'AP': 'HYDERABAD'}
>>> 
>>> 
>>> # Dict values can be dublicate
>>> 
>>> 
>>> # How to update existing key value
>>> # SYNATX:  dict_name[<key>] = <value>
>>> 
>>> ist["AP"] = "AMARAVATHI"
>>> 
>>> ist
{'KA': 'BANAGLORE', 'KL': 'TRIVENDRUM', 'TN': 'CHENNAI', 'TS': 'HYDERABAD', 'AP': 'AMARAVATHI'}
>>> 
>>> # Dict keys must be unique
>>> 
