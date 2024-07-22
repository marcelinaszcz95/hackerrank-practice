# Problem: https://www.hackerrank.com/challenges/most-commons/problem
# Score: 30

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':

    c = Counter(input())
    lista = ([i for i in c.items()])

    lista = sorted(lista)
    num_sorted = sorted(lista, key=lambda x: x[1], reverse=True)

    for item in num_sorted[:3]:
        print(f'{item[0]} {item[1]}')
