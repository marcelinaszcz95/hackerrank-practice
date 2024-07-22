# Problem: https://www.hackerrank.com/challenges/exceptions/problem
# Score: 10

inp = int(input())

for i in range(inp):
    try:
        a, b = map(int, input().split())

        print(int(a//b))
    except Exception as err:
        print("Error Code:", err)