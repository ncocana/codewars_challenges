#Kata in codewars: https://www.codewars.com/kata/5acbc3b3481ebb23a400007d

def is_flush(cards):
    
    return len(set([c[len(c)-1] for c in cards]))==1
    
    #Analisis of the code by parts to understand it better:
    
    #[c[len(c)-1] for c in cards]                = "c[len(c)-1]" returns the last character of every element (c) in the list "cards".
    #set([c[len(c)-1] for c in cards])           = "set()" eliminates the repeated letters if there are.
    #len(set([c[len(c)-1] for c in cards]))      = "len ()" returns the number of different elements/letters there are now.
    #len(set([c[len(c)-1] for c in cards]))==1   = If the number of elements/letters equals "1", returns True. Otherwise, returns "False".