# WAP find vowels from the given string


#str1 = "bangalore"

str1 = input("Enter a strin: ")
#vowels = ['a', 'e', 'i', 'o', 'u']
vowels = ('a', 'e', 'i', 'o', 'u')
for ch in str1:
     if ch in vowels:
          print(ch)
