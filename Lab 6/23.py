def to_upper(text):
    result = ""

    for ch in text:
        if 'a' <= ch <= 'z':
            result = result + chr(ord(ch) - 32)
        else:
            result = result + ch

    return result


text = input()
print(to_upper(text))
