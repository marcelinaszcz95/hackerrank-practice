# Problem: https://www.hackerrank.com/challenges/np-array-mathematics/problem
# Score: 20

import numpy
N, M = list(map(int, (input().split())))

matrix_1 = []
for i in range(N):
    row = (list(map(int, input().split())))
    matrix_1.append(row)

matrix_2 = []
for i in range(N):
    row = (list(map(int, input().split())))
    matrix_2.append(row)

M1, M2 = numpy.array(matrix_1), numpy.array(matrix_2)
print(numpy.add(M1, M2))
print(numpy.subtract(M1, M2))
print(numpy.multiply(M1, M2))
print(numpy.floor_divide(M1, M2))
print(numpy.mod(M1, M2))
print(numpy.power(M1, M2))