def to_camel_case(text):
    
    list = [char for char in text]
    #Seperates each character in the variable "text".
    
    if len(list) != 0:
        for i in range(len(list)):
            if list[i] in ('-', '_'):
                list[i+1] = list[i+1].upper()
    #Capitalizes the characters after '-' and '_'.
    
    list = ''.join([i for i in list if i not in ('-', '_')])
    #Joins all characters while removing the '-' and '_'.
    
    return list