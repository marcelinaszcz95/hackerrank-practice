# Problem: https://www.hackerrank.com/challenges/py-check-subset/problem
# Score: 10

T = int(input())

List_A = []
List_B = []

for c in range(T):
    nb_A = int(input())
    A = set(map(int, input().split()))
    List_A.append(A)

    nb_B = int(input())
    B = set(map(int, input().split()))
    List_B.append(B)

for i in range(T):
    if List_A[i].issubset(List_B[i]):
        print(True)
    else: print(False)
