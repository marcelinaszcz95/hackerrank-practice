# Problem: https://www.hackerrank.com/challenges/python-time-delta/problem
# Score: 30

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
    
from datetime import datetime

def time_delta(t1, t2):
    format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, format)
    t2 = datetime.strptime(t2, format)
    return str(int(abs((t1-t2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
