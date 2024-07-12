# Problem: https://www.hackerrank.com/challenges/capitalize/problem
# Score: 20


# Complete the solve function below.

def solve (s):
    ans = s.split(" ")
    capit = (a.capitalize() for a in ans)
    return " ".join(capit)