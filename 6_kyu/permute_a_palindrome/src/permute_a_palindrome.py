#Kata in codewars: https://www.codewars.com/kata/58ae6ae22c3aaafc58000079

def permute_a_palindrome (input): 
    
    return sum(input.count(c)%2 for c in set(input)) < 2
    #set(input)  - Sets apart each letter. ("baabcd")  -> {'b', 'd', 'a', 'c'}
    #input.count(c)%2  - Divides each letter by 2 and returns the remainder of the division.
    #If more than one letter repeats itself an odd number of times, it will return a number equal or bigger than 2, which will return False.
    
    #The reason for this is:
    #1. If the length is even, every unique character in the input has to occur a multiple of 2 times.
    #2. If the length is odd, every unique character except one has to occur a multiple of 2 times. Only 1 character is allowed to not occur a multiple of 2 times.
    
    #An example of brute force approach would be the next:
    """import itertools
    def permute_a_palindrome (input):
    
        permu = list(set(itertools.permutations(input)))

        result = input

        for pal in permu:
            if pal == pal[::-1]:
                result = ''.join(pal)

        return True if result == result[::-1] else False"""