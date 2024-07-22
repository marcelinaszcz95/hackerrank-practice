# Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem
# Score: 10

import cmath
n = input()
s = complex(n)
print(abs(s))
print(cmath.phase(s))