# Problem: https://www.hackerrank.com/challenges/np-polynomials/problem
# Score: 20

import numpy

M = list(map(float, (input().split())))
N=int(input())
val = numpy.polyval(M, N)
print(val)