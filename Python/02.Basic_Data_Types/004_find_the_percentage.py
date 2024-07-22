# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score: 10

for student in range(num_of_students):
    name, *grade_inp = input().split()
    grades = list(map(float, grade_inp))
    students_grades[name] = grades

query_name = input()
if query_name in students_grades:
    print('{:.2f}'.format(sum(students_grades[query_name])/len(students_grades[query_name])))