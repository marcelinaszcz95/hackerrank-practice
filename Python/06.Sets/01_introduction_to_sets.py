# Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Score: 10

def average(array):
    new_set = (set(array))
    suma = sum(new_set)
    nb = len(new_set)
    avg = suma/nb
    return ("%.3f" % avg)