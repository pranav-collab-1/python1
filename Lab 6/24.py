def count_character(text, ch):
    count = 0

    for x in text:
        if x == ch:
            count = count + 1

    return count


text = input()
ch = input()

print(count_character(text, ch))
