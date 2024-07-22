# Problem: https://www.hackerrank.com/challenges/compress-the-string/problem
# Score: 20

import itertools

def main(string):
    for k, g in itertools.groupby(string):
        print((len(list(g)), int(k)), end= ' ')

main(input())