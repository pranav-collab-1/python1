sentence = input("Enter a sentence: ")
v = ['a','e','i','o','u','A','E','I','O','U']
vowel = 0
consonant = 0
for i in sentence:
P a g e | 3
 if i in v:
 vowel += 1
 else:
 consonant += 1
print("Vowels:",vowel,"\nConsonants:",consonant)
