# Given a string, return the first recurring character. For instance, from 'ACBDBA', return 'B'. 

def recurring_character_first_attempt(word: str):
    start = 1

    for letter in word:
        if word.count(letter, start) > 0:
            return letter
        start = start + 1


    return ''

def recurring_character(word: str):

    ocurrences = set()
    for letter in word:
        if letter in ocurrences:
            return letter
        ocurrences.add(letter)

    return ''
