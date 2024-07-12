# Problem: https://www.hackerrank.com/challenges/python-tuples/problem
# Score: 10

n = int(input())

integer_list = (map(int, input().split()))
t = tuple(integer_list)

print((hash(t)))