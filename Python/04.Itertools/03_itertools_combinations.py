# Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem
# Score: 10

from itertools import combinations

str1, k = input().split()
str1=sorted(str1)

for i in range(1, int(k)+1):
    for j in (combinations(str1, i)):
        print("".join(j))
