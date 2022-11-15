import math

def square_area(A):
    
    a = A / (2 * math.pi * (90 / 360))
    area = math.pow(a, 2)
    
    return round(area,2)