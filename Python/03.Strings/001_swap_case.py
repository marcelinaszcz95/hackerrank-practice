# Problem: https://www.hackerrank.com/challenges/swap-case/problem
# Score: 10

def swap_case(s):
    return ''.join(char.lower() if char.isupper() else char.upper() for char in s)

s = input()
print(swap_case(s))