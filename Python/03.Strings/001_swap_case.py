# Problem: https://www.hackerrank.com/challenges/swap-case/problem
# Score: 10

def swap_case(s):
    lista = [char for char in s]    
    lista2 = []

    for letter in lista:
        if letter.islower():
            lista2.append(letter.upper())
        else:
            lista2.append(letter.lower())
    
    return ''.join(lista2)