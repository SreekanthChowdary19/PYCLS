# Write a program count each ovels of a charcater from the given string


str1 = "python-program-is-easy"

d = {}
for ch in str1:

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u': # o, o, a, i, e a
        # checking the vowel available in dict
        # if not avilable adding new key value pair , where the value is 1

        if ch not in d:
            d[ch] = 1   # d ={'o': 2, 'a':2, 'i': 1, 'e': 1}
        else:
            d[ch] = d[ch] +1
print(d)
    
     
 
    
