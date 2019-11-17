# WAP count number of vowels from the given string


str1 = "bangalore"
print("Input String: {}".format(str1))
count = 0
vowels = "aeiou"
for ch in str1:
     if ch in vowels:
         count = count +1
print("Vowel count: {}".format(count))
         
