# Problem: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Score: 20

from collections import OrderedDict

items = OrderedDict()

N = int(input())

for i in range(N):
    elements = input().split()
    count = int(elements.pop())
    name = " ".join(elements)
    if name in items:
        items[name] += count
    else:
        items[name] = count

for name, count in items.items():
    print(name, count)