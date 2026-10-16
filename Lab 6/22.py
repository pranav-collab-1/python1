def count_words(sentence):
    words = sentence.split()
    return len(words)


sentence = input()
print(count_words(sentence))
