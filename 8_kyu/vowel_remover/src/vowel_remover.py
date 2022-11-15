def shortcut( s ):
    
    no_vowels = ''.join(char for char in s if not char in 'aeiou')
    
    return no_vowels