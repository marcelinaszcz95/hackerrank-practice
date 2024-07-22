# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Score: 10

a=input()
numa = set(map(int, input().split()))
b = input()
numb = set(map(int, input().split()))

diffa = numa.difference(numb)
diffb = numb.difference(numa)

uni = list(diffa.union(diffb))
uni = sorted(uni)

for i in uni:
    print(i)