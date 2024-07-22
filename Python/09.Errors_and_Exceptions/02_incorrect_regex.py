# Problem: https://www.hackerrank.com/challenges/incorrect-regex/problem
# Score: 20

import re
n = int(input())
for i in range(n):  
    try:
        input_ = input()
        a = (re.compile(input_))
        print(bool(a))
    except re.error:
        print('False')