# Problem: https://www.hackerrank.com/challenges/np-linear-algebra/problem
# Score: 20

import numpy

N = int(input())
M= []
for i in range(N):
    row = list(map(float, input().split()))
    M.append(row)
M = numpy.array(M)
print(round(numpy.linalg.det(M), 2))