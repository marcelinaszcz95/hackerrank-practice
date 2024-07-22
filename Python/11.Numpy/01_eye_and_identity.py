# Problem: https://www.hackerrank.com/challenges/np-eye-and-identity/problem
# Score: 20

import numpy

numpy.set_printoptions(legacy="1.13")
n = list(map(int, input().split()))
print(numpy.eye(n[0], n[1]))
