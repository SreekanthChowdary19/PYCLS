Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> import re
>>> 
>>> 
>>> str1 = "The timer will starts at time 12PM"
>>> 
>>> re.findall('\w{4}', str1)
['time', 'will', 'star', 'time', '12PM']
>>> re.findall('\b\w{4}\b', str1)
[]
>>> re.findall(r'\b\w{4}\b', str1)
['will', 'time', '12PM']
>>> 
>>> dir(re)
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'Match', 'Pattern', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pickle', '_special_chars_map', '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
>>> # search will search entire text
>>> # match will search only starting of the text
>>> re.match(r"The", str1)
<re.Match object; span=(0, 3), match='The'>
>>> re.search(r"The", str1)
<re.Match object; span=(0, 3), match='The'>
>>> re.search(r"at", str1)
<re.Match object; span=(22, 24), match='at'>
>>> re.match(r"at", str1)
>>> 
>>> 
>>> 
>>> 
>>> re.sub(r'\btime\b', "TM", str1)
'The timer will starts at TM 12PM'
>>> 
>>> 
>>> 
