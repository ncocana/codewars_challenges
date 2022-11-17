#Kata in codewars: https://www.codewars.com/kata/5aec1ed7de4c7f3517000079

def first_n_smallest(arr, n):
    
    result=[]
    #Creates a list.
    
    sorted_arr = sorted(arr)[:n]
    #Sorts the numbers from smallest to bigger and saves the firsts 'n' (variable of number).
    
    for num in arr:
        if num in sorted_arr:
            result.append(num)
            #If the number (num) is in 'sorted_arr', append it to 'result'.

            sorted_arr.pop(sorted_arr.index(num))
            #Gets the sorted list of the firsts 'n' numbers and eliminates the 'num' out of it.
            #When 'sorted_arr' runs out of numbers/elements, it will stop appending them to 'result'.
            #Without this line, result.append(num) sometimes ends up appending more numbers than it should or appending some wrong ones.
    
    return result