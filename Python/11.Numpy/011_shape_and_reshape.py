# Problem: https://www.hackerrank.com/challenges/np-shape-reshape/problem
# Score: 20

import numpy

new_array = list(map(int, input().split(' ')))
print(numpy.reshape(new_array, (3,3)))