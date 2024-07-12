# Problem: https://www.hackerrank.com/challenges/python-print/problem
# Score: 20

n = int(input())
if 1 <= n <= 150:
    lista = list(range(1, n+1))
    s = ''.join(str(x) for x in lista)
    print(s)
