def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            vowels = vowels + 1
        elif ch.isalpha():
            consonants = consonants + 1

    return vowels, consonants


text = input("Enter string: ")
v, c = count_vowels_consonants(text)

print(v)
print(c)
