# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Score: 10

from itertools import combinations_with_replacement

str, numb = input().split()
numb = int(numb)
str = sorted(str)
str_sorted = ''.join(str)

lista = list(combinations_with_replacement(str_sorted, numb))

for item in lista:
    print(''.join(item))