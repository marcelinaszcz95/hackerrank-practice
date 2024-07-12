# Problem: https://www.hackerrank.com/challenges/python-lists/problem
# Score: 10

N = int(input())
lista=[]
for c in range(N):
    command = input().split() # gives list with 2 elements str
    if command[0] =="append":
        lista.append(int(command[1]))
    elif command[0] == "insert":
        lista.insert(int(command[1]), int(command[2]))
    elif command[0] == "pop":
        lista.pop()
    elif command[0] == "print":
        print(lista)
    elif command[0] == "remove":
        lista.remove(int(command[1]))
    elif command[0] == "sort":
        lista.sort()
    elif command[0] == "reverse":
        lista.reverse()
