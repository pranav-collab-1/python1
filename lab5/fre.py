# Question 1
sentence = input("Enter a sentence: ")
a = {}
for ch in sentence:
 if ch in a:
 a[ch] += 1
 else:
 a[ch] = 1
for ch,count in a.items():
 print(f"'{ch}': {count}")
