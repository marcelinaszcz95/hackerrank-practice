# Problem: https://www.hackerrank.com/challenges/hex-color-code/problem
# Score: 30

import re

pattern = re.compile(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})')
for _ in range(int(input())):
    matches = re.findall(pattern, input())
    if matches:
        print(*matches, sep='\n')