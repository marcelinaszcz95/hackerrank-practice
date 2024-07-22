# Problem: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Score: 20

from collections import namedtuple
input_ = int(input())
my_fields = input().split()
total_marks = 0
for _ in range(input_):
    students = namedtuple('my_student', my_fields)
    M, C, N, ID = input().split()
    my_student = students(M, C, N, ID)
    total_marks += int(my_student.MARKS)
print((total_marks / input_))