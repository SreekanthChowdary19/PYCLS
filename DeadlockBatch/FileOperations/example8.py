# WAP count each occurance of a character from the given string

str1 = "python-program-is-easy"

d = {}
for ch in str1:
        if ch not in d:
            d[ch] = 1   # d ={'o': 2, 'a':2, 'i': 1, 'e': 1}
        else:
            d[ch] = d[ch] +1
print(d)
    
