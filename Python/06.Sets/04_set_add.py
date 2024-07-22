# Problem: https://www.hackerrank.com/challenges/py-set-add/problem
# Score: 10

N = int(input())
s = set()

for i in range(N):
    country = input()
    s.add(country)
print(len(s))