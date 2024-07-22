# Problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Score: 10

E = int(input())
students_E = set(map(str, input().split()))
F = int(input())
students_F = set(map(str, input().split()))

sym_dif = (students_F.symmetric_difference(students_E))
print(len(sym_dif))