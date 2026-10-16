def reverse_string(text):
    rev = ""

    for ch in text:
        rev = ch + rev

    return rev


text = input()
print(reverse_string(text))
