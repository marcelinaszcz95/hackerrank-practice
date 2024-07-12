# Problem: https://www.hackerrank.com/challenges/designer-door-mat/problem
# Score: 10

N, M = map(int, input().split())

m= int((M-3)/2)

r = int(N//2)
d = int((M-3)/2)
for i in range(r):
    print(('-'*((m)-(i*3)))+('.|.'*(2*i+1))+('-'*((m)-(i*3))))
text = "WELCOME"
print(text.center(M,"-"))

for i in reversed(range(r)):
    print(('-'*((m)-(i*3)))+('.|.'*(2*i+1))+('-'*((m)-(i*3))))