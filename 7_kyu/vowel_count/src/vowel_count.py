#Kata in codewars: https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    
    vowels_string = ''.join(char for char in sentence if char in 'aeiou')
            
    return len(vowels_string)