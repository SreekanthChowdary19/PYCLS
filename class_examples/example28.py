# WAP count each vowel from the given string


str1 = "bangalore-hyderabad"
"""
for ch in str1:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print(ch)
    #print(ch)

"""
"""
vowels = ['a', 'e', 'i', 'o', 'u']
for ch in str1:
    if ch in vowels:
        print(ch)
"""


str1 = "hyderabad-bangalore"
vowels = ('a', 'e', 'i', 'o', 'u')
d = {} # Place holder to store the output
for ch in str1:
    if ch in vowels:
        if ch not in d:
            d[ch] = 1  # d = {'e':1, 'a':2}
        else:
            d[ch] = d[ch] +1
        
       
print(d)

#d = {"A": 65, "B": 66, "C": 68}
"""
for i in d:
    print(i)



for i in d:
    print(d[i])


for key in d.keys():
    print(key)


for val in d.values():
    print(val)
"""
