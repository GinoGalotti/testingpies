# Given an input string, reverse all the words. 
# To clarify, input: "Interviews are awesome!" output: "awesome! are Interviews". 
# Consider all consecutive non-whitespace characters as individual words. 
# If there are multiple spaces between words reduce them to a single white space. 
# Also remove all leading and trailing whitespaces. 
# So, the output for " CS degree", "CS degree", "CS degree ", or " CS degree " 
# are all the same: "degree CS".

def reverse(phrase: str):
    words = phrase.split()

    words.reverse()

    return " ".join(str(e) for e in words)

# Assuming I can't use reverse
def reverse_old_way(phrase: str):
    words = phrase.split()
    
    reversed_phrase = []
    for element in words: 
        reversed_phrase.insert(0, element)

    return " ".join(str(e) for e in reversed_phrase)