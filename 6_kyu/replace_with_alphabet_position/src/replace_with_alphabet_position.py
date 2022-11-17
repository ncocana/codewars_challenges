#Kata in codewars: https://www.codewars.com/kata/546f922b54af40e1e90001da

import string
#Imports the Python's string library.

def alphabet_position(text):
    
    alphabet = {v:k for k, v in enumerate(string.ascii_lowercase, start=1)}
    #Links and associates every letter (key) with a number (value), which starts from number 1 and continues so with [enumerate()]: {'a': 1, 'b': 2, 'c': 3, 'd': 4, ...}.
    
    return ' '.join(str(alphabet.get(char)) for char in text.lower() if char in alphabet.keys())
    #First converts all the uppercase letters in lowecase with [text.lower()].
    #Then gets the number (value) associated with every character (key) in the text and converts it to a string: [str(alphabet.get(char)) for char].
    #But only gets the number (value) if the character (key) is in the variable [alphabet].
    #Finally, returns the numbers joined and seperated with a space with [' '.join()].