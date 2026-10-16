def reverse_string(text):
    rev = ""

    for ch in text:
        rev = ch + rev

    return rev


def is_palindrome(text):
    if text == reverse_string(text):
        return True
    else:
        return False


text = input()
print(is_palindrome(text))
