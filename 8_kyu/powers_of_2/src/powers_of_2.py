def powers_of_two(n):
    
    power = 0
    list = []
    
    while power != n+1:
        list.append(2**power)
        power += 1
    
    return list