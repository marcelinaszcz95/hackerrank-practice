# Problem: https://www.hackerrank.com/challenges/calendar-module/problem
# Score: 10

import calendar
date_inp = list(map(int, input().split()))
weekday = calendar.weekday(date_inp[2], date_inp[0], date_inp[1])

if weekday == 0:
    print("MONDAY")
if weekday == 1:
    print("TUESDAY")
if weekday == 2:
    print("WEDNESDAY")
if weekday == 3:
    print("THURSDAY")
if weekday == 4:
    print("FRIDAY")
if weekday == 5:
    print("SATURDAY")
if weekday == 6:
    print("SUNDAY")
