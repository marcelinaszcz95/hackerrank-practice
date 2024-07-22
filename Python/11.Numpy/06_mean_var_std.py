# Problem: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
# Score: 20

import numpy
N, M = list(map(int, (input().split())))


matrix_1 = []
for i in range(N):
    row = (list(map(int, input().split())))
    matrix_1.append(row)

mean = print(numpy.mean(matrix_1, axis=1))
var = print(numpy.var(matrix_1, axis=0))
print(round(numpy.std(matrix_1, axis=None), 11))