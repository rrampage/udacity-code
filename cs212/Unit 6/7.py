# cs212 ; Unit 6 ; 7
# -----------------
# User Instructions
# 
# Write a function, extend_prefix, nested in find_words,
# that checks to see if the prefix is in WORDS and 
# adds that to results if it is.
#
# If not, your function should check to see if the prefix
# is in PREFIXES, and if it is should recursively add letters
# until the prefix is no longer valid.

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

def readwordlist(filename):
    file = open(filename)
    text = file.read().upper()
    wordset = set(word for word in text.splitlines())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset
    
WORDS, PREFIXES = readwordlist('words4k.txt')

def find_words(letters):
    results = set()

    def extend_prefix(w, letters):
        if w in WORDS: ###Your code here.
        if w not in PREFIXES: return
        for L in letters:
            ###Your code here.

    extend_prefix('', letters)
    return results
