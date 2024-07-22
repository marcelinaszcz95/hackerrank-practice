# Problem: https://www.hackerrank.com/challenges/np-dot-and-cross/problem
# Score: 20

import numpy
N = int(input())

matrix_1 = []
for i in range(N):
    row = (list(map(int, input().split())))
    matrix_1.append(row)
matrix_2 = []
for i in range(N):
    row = (list(map(int, input().split())))
    matrix_2.append(row)

m = numpy.dot(matrix_1, matrix_2)
print(m)
