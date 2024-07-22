# Problem: https://www.hackerrank.com/challenges/collections-counter/problem
# Score: 10

from collections import Counter
X = int(input())
all_sizes = list(map(int, input().split()))
N = int(input())

orders = []
for i in range(0, N):
    item = list(map(int, input().split()))
    orders.append(item)

total = []
for i in range(0,N):
    if orders[i][0] in all_sizes:
        total.append(orders[i][1])
        all_sizes.remove(orders[i][0])

print(sum(total))
