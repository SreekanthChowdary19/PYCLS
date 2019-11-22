#  How to process text files , today we will understnd processing the JSON data
"""
JSON : Its JAVA SCRIPT OBJECT NOTATION

Its Light waight data interchange format

It may looks like python dictionary

or

It may looks like python list
"""
import json


f = open('input.json', 'r')
data = f.read()
f.close()

#print(type(data))

#print(data)

data = json.loads(data) #? Converting JSON data to PYTHON Dict
print(type(data))
print(data["glossary"]["title"])
print(data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["ID"])

