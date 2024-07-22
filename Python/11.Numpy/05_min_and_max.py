# Problem: https://www.hackerrank.com/challenges/np-min-and-max/problem
# Score: 20

import numpy
N, M = list(map(int, (input().split())))

matrix_1 = []
for i in range(N):
    row = (list(map(int, input().split())))
    matrix_1.append(row)

mini = numpy.min(matrix_1, axis = 1)
max = max(mini)
print(max)