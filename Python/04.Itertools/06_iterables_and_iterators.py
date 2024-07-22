# Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Score: 40

from itertools import combinations
N= int(input())
lista = list(input().split())
M = int(input())
comb = (list(combinations(lista, M)))

counter = 0

for i in comb:
    if "a" in i:
        counter += 1

probability = round(counter/len(comb), 3)
print(probability)
