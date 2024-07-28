# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Score: 10


A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    ans=True
    ans=A.issuperset((set(map(int, input().split()))))
    if ans == False:
        break
print(ans)