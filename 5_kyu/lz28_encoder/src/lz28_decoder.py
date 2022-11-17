#Kata in codewars: https://www.codewars.com/kata/5db42a943c3c65001dcedb1a

def decoder(data):
    
    dictionary = {0: ''}
    counter_dict = 1
    key = ''
    result = []
    
    for char in data:
        if char.isdigit():
            key += char
        else:
            letter_string = dictionary[int(key)] + char
            dictionary[counter_dict] = letter_string
            counter_dict += 1
            result.append(letter_string)
            key = ''
    if key != '':
        result.append(dictionary[int(key)])
    return ''.join(result)
