# Problem: https://www.hackerrank.com/challenges/np-inner-and-outer/problem
# Score: 20

import numpy

row1 = (list(map(int, input().split())))
row2 = (list(map(int, input().split())))

m = numpy.inner(row1, row2)
print(m)
o = numpy.outer(row1, row2)
print(o)