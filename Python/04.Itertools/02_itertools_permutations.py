# Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Score: 10

from itertools import permutations
str1, ind = input().split()

for i in sorted(list(permutations(str1, int(ind)))):
    print("".join(i))