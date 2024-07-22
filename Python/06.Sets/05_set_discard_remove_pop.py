# Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Score: 10

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    com = input().split()
    if com[0] == "pop":
        s.pop()
    elif com[0] == "remove":
        s.remove(int(com[1]))
    elif com[0] == "discard":
        s.discard(int(com[1]))
print(sum(s))