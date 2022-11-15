def anagrams(word, words):
    
    match = sorted(word)
    #Seperates each character in the variable "word".
    
    return [anagram for anagram in words if match == sorted(anagram)]
    #Seperates each character in each anagram in the variable "words". If the charachters in "word" are in one of the anagrams of "words", then returns that anagram.