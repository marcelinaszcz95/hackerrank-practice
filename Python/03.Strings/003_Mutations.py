# Problem: https://www.hackerrank.com/challenges/python-mutations/problem
# Score: 10

def mutate_string(string, position, character):
    lista = [char for char in string]
    lista[position]=character
    new_string = ''.join(lista)
    return new_string