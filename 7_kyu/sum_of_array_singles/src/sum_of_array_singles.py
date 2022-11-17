#Kata in codewars: https://www.codewars.com/kata/59f11118a5e129e591000134

def repeats(arr):
    return sum(x for x in arr if arr.count(x) == 1)