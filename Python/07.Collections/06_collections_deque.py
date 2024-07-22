# Problem: https://www.hackerrank.com/challenges/py-collections-deque/problem
# Score: 20

from collections import deque
d = deque()
for i in range(int(input())):
    
    operation, *number = input().split()
    if number:
        num1 = int(number[0])
    if operation == 'append':
        d.append(num1)
    elif operation == 'appendleft':
        d.appendleft(num1)
    elif operation == 'pop':
        d.pop()
    elif operation == 'popleft':
        d.popleft()
    
for i in range(len(d)):
    print(d.popleft(), end = ' ')
