# Problem: https://www.hackerrank.com/challenges/write-a-function/problem
# Score: 10


def is_leap(year):
  leap = False
  if 1900 <= year <= 10000 and year % 400 == 0 and year % 4 ==0:
      leap = True
  elif 1900 <= year <= 10000 and year % 4 ==0 and year % 100 != 0:
      leap = True
  return leap


year = 1990
print(is_leap(year))