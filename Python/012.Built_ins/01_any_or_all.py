# Problem: https://www.hackerrank.com/challenges/any-or-all/problem
# Score: 20

N = int(input())
ans = False
lista = list(map(int, input().split()))

pos = True
for e in lista:
    if e<0:
        pos=False
lista = map(str, lista)
for e in lista:
    if list(e) == list(reversed(e)):
        ans=True
        break
            
print(any([ans]) and all([pos]))