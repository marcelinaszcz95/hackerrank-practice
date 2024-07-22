# Problem: https://www.hackerrank.com/challenges/find-angle/problem
# Score: 10

from math import degrees, atan2

AB = float(input())
BC = float(input())

MBC = round(degrees(atan2(AB, BC)))
print((str(MBC)), chr(176), sep='')