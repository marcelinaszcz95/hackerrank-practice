# Problem: https://www.hackerrank.com/challenges/py-if-else/problem
# Score: 10

n = int(input().strip())
if n%2 != 0:
    print("Weird")
elif n%2 == 0 and 2<= n <= 5:
    print("Not Weird")
elif n%2 == 0 and 6<= n <= 20:
    print("Weird")
elif n%2 == 0 and n>20:
    print("Not Weird")
