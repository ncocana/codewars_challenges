def get_count(sentence):
    
    vowels_string = ''.join(char for char in sentence if char in 'aeiou')
            
    return len(vowels_string)