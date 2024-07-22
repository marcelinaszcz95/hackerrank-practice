# Problem: https://www.hackerrank.com/challenges/maximize-it/problem
# Score: 50

from itertools import product
K, M = list(map(int, (input().split())))
N = []
for i in range(K):
    N.append(list(map(int, input().split()))[1:])

print(max(((sum(x**2 for x in c)% M) for c in product(*N))))