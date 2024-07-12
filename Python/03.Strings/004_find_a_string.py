# Problem: https://www.hackerrank.com/challenges/find-a-string/problem
# Score: 10

def count_substring(string, sub_string):
    total = 0

    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(sub_string):
            total += 1
    return total