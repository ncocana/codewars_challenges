#Kata in codewars: https://www.codewars.com/kata/59706036f6e5d1e22d000016

def words_to_marks(s):
    
    alphabet = list(map(chr, range(97, 123)))
    #Creates a list with the lowercase alphabet.
    
    letter_number = {v:k for k,v in enumerate(alphabet,1)}
    #Links every letter with a number.
    
    return sum(letter_number[x] for x in s)
    #Returns the sum of the word.