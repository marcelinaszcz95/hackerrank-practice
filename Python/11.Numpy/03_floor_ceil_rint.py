# Problem: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
# Score: 20

import numpy
numpy.set_printoptions(legacy = '1.13')
lista = list(map(float, input().split()))


print(numpy.floor(lista))
print(numpy.ceil(lista))
print(numpy.rint(lista))
