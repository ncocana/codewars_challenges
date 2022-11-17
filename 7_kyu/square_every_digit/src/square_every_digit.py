#Kata in codewars: https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    
    list = [int(x) for x in str(num)]
    #Separates the numbers in "num" while converting them to integer.
    
    square = [x**2 for x in list]
    #Raise to power 2 the numbers.
    
    string = [str(x) for x in square]
    #Convert the numbers from integer to string.
    
    result = int(''.join(string))
    #Joins the numbers again and converts them to integer so they appear without the '' ('[number]').

    return result
    #Returns the final result.