
# This function will break up words for us in their typed order.
def break_words(stuff):
    words = stuff.split(' ')
    return words

# This function sorts the words into a list of letters in alphabetical order.
def sort_words(words):
    return sorted(words)

# This function prints the first word after popping it off.
def print_first_word(words):
    #Note: definition of pooping it?
    word = words.pop(0)
    print(word)

# Prints the last word after popping it off.
def print_last_word(words):
    word = words.pop(-1)
    print(word)

# Takes the full sentence then returns / prints the sorted letters used alphabetially
def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

# Prints the first and the last word of the sentence
def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# Sorts the words alphabetically then prints the first and last one
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#Study Drills:

# 1. Take the remainng lines of the What You Should See output and figure out What
# they are doing. Make sure you understand how you are running your functions in the
# ex25 module.
# 1 - a: This takes all the words and sorted them alphabetially then prints only
# the first and last word from the sorted list.
# 2. Try doing this: help (ex25) and also help(ex25.break_words).
