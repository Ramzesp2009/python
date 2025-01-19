def add_underscores(word):
    new_word = "_"
    for letter in word:
        new_word = new_word + letter + "_"
    return new_word

phrase = "HelloWord"
print(add_underscores(phrase))
