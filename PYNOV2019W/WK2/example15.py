# WAP count each occurance of a vowel from the given string


str1 = "banaglore"

vowels = "aeiou"
d = {} # Its a place holder to store the output
for ch in str1:
     if ch in vowels: # aaoe
          if ch not in d:
              d[ch] = 1  # {'a':1}
          else:
              d[ch] = d[ch] +1
print(d)
         
          
     
