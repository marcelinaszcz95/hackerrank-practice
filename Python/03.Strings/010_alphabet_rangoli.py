# Problem: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# Score: 20

import string
f = string.ascii_lowercase
def print_rangoli(size):
    w = (2*size)-1
    l = (2*w)-1
    lines = []
    for row in range(size):
        print_ = "-".join(f[row:size])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])

    for row in range(size-1, 0, -1):
        print(lines[row].center(l,'-'))
    for row in range(size):
        print(lines[row].center(l, '-'))

