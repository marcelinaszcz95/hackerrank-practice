# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Score: 10

students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

grades_list = sorted(list(set([stu[1] for stu in students])))
second_lower = grades_list[1]

students_with_second_lowest = sorted([stu[0] for stu in students if stu[1]==second_lower])

for name1 in students_with_second_lowest:
    print(name1)