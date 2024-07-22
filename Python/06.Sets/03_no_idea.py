# Problem: https://www.hackerrank.com/challenges/no-idea/problem
# Score: 50

n, m = map(int, input().split())
arr = (map(int, input().strip().split()))

l1= set(map(int, input().strip().split()))
l2= set(map(int, input().strip().split()))

counter=0

for i in arr:
    if i in l1:
        counter += 1
    elif i in l2:
        counter -= 1

print(counter)