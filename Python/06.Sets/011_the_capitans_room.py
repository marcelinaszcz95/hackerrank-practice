# Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Score: 10

from collections import Counter
K = int(input())
a = list(map(int, input().split()))
c=(Counter(a))

def get_key_from_value(dictionary, value):
    inverted_dict = {v: k for k, v in dictionary.items()}
    return inverted_dict.get(value)

my_dict = c
value = 1
key = get_key_from_value(my_dict, value)
print(key)

