# Problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Score: 10

eng = int(input())
stu_eng = set(map( int, input().split()))
fre = int(input())
stu_fre = set(map( int, input().split()))

total_sub = stu_eng.difference(stu_fre)
print(len(total_sub))