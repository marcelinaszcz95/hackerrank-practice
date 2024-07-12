# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score: 10


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

suma = (sum(student_marks[query_name]))
nb_of_marks = len(student_marks[name])
avg = suma/nb_of_marks
print('{:.2f}'.format(avg))