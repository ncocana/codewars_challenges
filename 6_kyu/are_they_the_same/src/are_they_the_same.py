def comp(array1, array2):
    
    array1_squared = []
    #Creates an empty array.
    
    if array1 == None or array2 == None:
        return False
        #Returns False is one of the arrays is NoneType.
    else:
        for num in array1:
            array1_squared.append(num**2)
            #Squares each number in array1 and appends it to the new array (array1_squared).
            
        if sorted(array1_squared) == sorted(array2):
            return True
        else:
            return False
        #Sorts each array so when they are compared, doesn't give False despite the elements being the same but not their order in the array.