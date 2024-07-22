# Problem: https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# Score: 20

import numpy
N, M = list(map(int, (input().split())))


matrix_1 = []
for i in range(N):
    row = (list(map(int, input().split())))
    matrix_1.append(row)

suma = numpy.sum(matrix_1, axis = 0)
product = numpy.prod(suma)
print(product)