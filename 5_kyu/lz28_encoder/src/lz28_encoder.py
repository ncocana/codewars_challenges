def encoder(data):
    
    dictionary = {0: ''}
    counter_dict = 1
    letter_string = ''
    result = []
    
    def get_key_by_value(value):
        
        for key in dictionary:
            if dictionary[key] == value:
                return key
    
    for letter in data:
        letter_string += letter
        if letter_string not in dictionary.values():
            dictionary[counter_dict] = letter_string
            result.append(str(get_key_by_value(letter_string[:-1])))
            result.append(letter_string[-1])
            counter_dict += 1
            letter_string = ''
    if letter_string != '':
        result.append(str(get_key_by_value(letter_string)))
    
    return ''.join(result)
