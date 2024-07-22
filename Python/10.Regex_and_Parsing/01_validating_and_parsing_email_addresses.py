# Problem: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# Score: 20

import email.utils
import re

num = int(input())
pattern = (r'^[A-Za-z][\w\.-]+@[A-Za-z]+\.[A-Za-z]{1,3}$')

for i in range(num):
    address = input()
    parsed = email.utils.parseaddr(address)
    if re.match(pattern, parsed[1]):
        print(email.utils.formataddr(parsed))